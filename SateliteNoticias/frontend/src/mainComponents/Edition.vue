<template>

<div >
    

          <md-drawer class="md-right" :md-active.sync="showSidepanel"  md-persistent="full" >
      
             <!-- EDITION COMPONENT -->
                  <md-toolbar class="md-transparent" md-elevation="2">

                      <md-button class="md-icon-button md-dense" @click="toggleMenu(false)" style="margin-left:auto">
                          <b-icon-x variant="danger" font-scale="7.5"></b-icon-x>                   
                       </md-button>
                  </md-toolbar>
                    <div style="padding: 1em"></div>
                <div :key="updateEditions">
                        <form style="   width: 85%;
                                      height: 85%;
                                      margin-right: auto;
                                      margin-left: auto; border: 1px solid blue" 
                                      @submit.prevent="onSubmit">
                            <NewsEdition @news-change="newsChange" :title="title" :body="body"></NewsEdition>
                            
                            <div style="padding: 1em"></div>

                            <PrimaryTagsEdition @primary-tags-change="primaryTagsEditionChange" :tags="tags"></PrimaryTagsEdition>
                            
                            <div style="padding: 1em"></div>

                            <SecondaryTagsEdition @secondary-tags-change="secondaryTagsEditionChange" :secondaryTags="tags"></SecondaryTagsEdition>
                            
                            <div style="padding: 1em"></div>

                            <BibliographyEdition @bibliography-change="bibliographyEditionChange" :bibliographyName="bibliographyName" :bibliographyLink="bibliographyLink"></BibliographyEdition>
                            
                            <div style="width: 100%; text-align:center;  margin-left:auto;margin-right:auto; padding:2em">
                                      
                                      <div class="button">
                                                <b-button  lg="4" variant="primary" type="submit">Publicar</b-button>
                                      </div>
                            </div>
                      
                      </form>
                  
                  
                  
                  
                </div>  
            

                  
                  <!-- EDITION COMPONENT -->

           </md-drawer>
  </div>
 
</template>
<script>

import NewsEdition from "@/miniComponents/edition/NewsEdition.vue";
import BibliographyEdition from "@/miniComponents/edition/BibliographyEdition.vue";
import PrimaryTagsEdition from "@/miniComponents/edition/PrimaryTagsEdition.vue";
import SecondaryTagsEdition from "@/miniComponents/edition/SecondaryTagsEdition.vue";

import { BIconX } from 'bootstrap-vue'

import { apiService } from "@/common/api.service.js";

export default {
  name: "Edition",
  props:{
      showPanel:Boolean,
      slug:String
  },
  components: {
    
    NewsEdition,
    BibliographyEdition,
    PrimaryTagsEdition,
    SecondaryTagsEdition,
    BIconX
    
  },
  computed: {
      changeData() {
        const { title, body,tags,bibliographyName,bibliographyLink } = this
        return {
          title,
          body,
          tags,
          bibliographyName,
          bibliographyLink
        }
      }
  },
  watch: {
    // whenever question changes, this function will run
    changeData: {
        handler: function(val) {
          console.log('value change: ', val)
          this.debouncedGetEditions()
        },
        deep: true
      }
  },

  data: () => ({
    showNavigation: false,
    showSidepanel: false,
    specificEdition:null,
    title: '',
    body:'',
    tags:[],
    bibliographyName: '',
    bibliographyLink:'',
    newsTags:null,
    editions:[],
    updateEditions:0,
    firstTime:false
  }),

  methods:{
      toggleMenu(bool){
          this.showSidepanel =  !this.showSidepanel
          if(bool){
            this.$emit("hide-panel",this.bibliographyName,this.bibliographyLink,this.slug,this.tags)

          }
          else{
            this.$emit("hide-panel",this.bibliographyName,this.bibliographyLink,"",this.tags)

          }
          //console.log(this.newsTags)
      },
      newsChange(title,body){
        this.title = title
        this.body= body
        //console.log(title)
        //console.log(body)
      },
      primaryTagsEditionChange(primaryTags){
        this.tags = primaryTags
        //console.log(primaryTags)
      },
      secondaryTagsEditionChange(secondaryTags){
        this.tags = secondaryTags
        //console.log(secondaryTags)
      },
      bibliographyEditionChange(names,links){
        this.bibliographyName = names
        this.bibliographyLink = links
        //console.log(this.bibliographyName)
        //console.log(this.bibliographyLink)

      },

       getnewsData() {
        // get the details of a news instance from the REST API and call setPageTitle
        let endpoint = `/api/news/${this.slug}/`;
        apiService(endpoint).then(data => {
          if (data) {
              //console.log('paso por aqui')
              //console.log(data.title)
              this.title = data.title
              this.body = data.content
              
              var method = "";
            
              method = "POST"
              
              let endpoint = `/api/news/${this.slug}/edition/`;
              //console.log('estos son los resultados')
              //console.log(this.bibliographyName)
              //console.log(this.bibliographyLink)
               var tagsAux = []
               console.log(this.tags)
               console.log(this.tags.length)
                for(var i=0;i<this.tags.length;i++){
                  this.$set(tagsAux, i, this.tags[i].text)

                }
              apiService(endpoint, method, { title: this.title,body: this.body, tags: tagsAux, bibliography_name: this.bibliographyName, bibliography_link: this.bibliographyLink}).then(
                data => {
                  console.log('este es la data que me entrego cuando creo una nueva edicion')
                  console.log(data)
                  this.editions.unshift(data);
                  this.setEdition(true)
                }
              );
                this.body = null;
                this.userHasEditioned = true;
                if (this.error) {
                  this.error = null;
                }
              else {
                this.error = "You can't send an empty edition!";
              }
          } 
          else {
            this.newsTags = null;
            this.setPageTitle("404 - Page Not Found");
          }
        });
      },
      
      onSubmit() {
        // Tell the REST API to create a new edition for this news based on the user input, then update some data properties
        
        //console.log('aqui voy a enviar una edition nueva')
        //console.log(this.slug)
        //console.log(this.tags)
        //console.log('aqui va los tags')
        var i = 0
        var tagsAux = []
        console.log(this.tags)
        if(this.tags !== undefined){
          
          if(this.tags[i].text !== undefined){
              for(i=0;i<this.tags.length;i++){
                  this.$set(tagsAux, i, this.tags[i].text)

               }
          }
          else{
                 for(i=0;i<this.tags.length;i++){
                    this.$set(tagsAux, i, this.tags[i])

              }
          }
          
        }
        //console.log(tagsAux)

        var method = "";
       
        method = "POST"
         
        let endpoint = `/api/news/${this.slug}/edition/`;
        //console.log('estos son los resultados')
        //console.log(this.bibliographyName)
        //console.log(this.bibliographyLink)
        console.log(tagsAux)
        apiService(endpoint, method, { title: this.title,body: this.body, tags: tagsAux, bibliography_name: this.bibliographyName, bibliography_link: this.bibliographyLink}).then(
          data => {
            console.log('este es la data que me entrego al responder la pregunta')
            console.log(data)
            this.editions.unshift(data);
            this.toggleMenu(true)
          }
        );
          this.body = null;
          this.userHasEditioned = true;
          if (this.error) {
            this.error = null;
          }
         else {
          this.error = "You can't send an empty edition!";
         }
      
      },
      
      comparingEditions(newEdition){
        if(this.editions !== undefined){
          if(this.editions.length === 0) return false
          var actualEdition = this.editions[0]
          console.log('Estos son los editions')
          console.log(actualEdition)
          console.log(newEdition)
          if(!(_.isEqual(actualEdition,newEdition[0]))) return true
               return false

          }
        
        },
        getnewsEditions() {
          // get a page of editions for a single news from the REST API's paginated 'news Endpoint'
          //console.log(this.slug)
          console.log('trying')
          let endpoint = `/api/news/${this.slug}/editions/`;
          apiService(endpoint).then(data => {
            if(data.results !== undefined){
                if(data.results.length ===0){
                        this.setEdition(false)
                      return
                }
                else if(this.comparingEditions(data.results)){
                    this.editions.splice(0)
                                    this.editions.push(...data.results);
                                    console.log(data.results)
                                    alert('ALGUIEN HA MODIFICADO LA NOTICIA, SU NOMBRE ES: ',data.results[0].author  )
                                    alert(data.results[0].author  )

                                                this.setEdition(true)
            

                  

                }
                else if(this.firstTime){
                       this.editions.push(...data.results);
                        this.setEdition(true)
                        this.firstTime = false
                }
            }
           

          });
        },
      setEdition(bool){        
        if(bool){
          this.specificEdition = this.editions[0]    
          this.title = this.specificEdition.title
          this.body = this.specificEdition.body
          this.tags = this.specificEdition.tags
          this.bibliographyName = this.specificEdition.bibliography_name
          this.bibliographyLink = this.specificEdition.bibliography_link
          this.updateEditions +=1
        }
        else{
           this.getnewsData()

        }

       
      }
  },
  created(){
    this.showSidepanel = this.showPanel
    this.firstTime = true
    this.getnewsEditions()

    //console.log('aqui va algo 2')
    //console.log(this.$props)

    this.debouncedGetEditions = _.debounce(this.getnewsEditions, 10000)

  }
};
</script>
<style scoped>
 .page-container {
    min-height: 300px;
    overflow: hidden;
    position: relative;
    border: 1px solid rgba(#000, .12);
  }

  .md-drawer {
    width: 35%;
    max-width: 100vw;
  }

  .md-content {
    padding: 16px;
  }

</style>