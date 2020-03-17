<template>

<div >
    

          <md-drawer class="md-right" :md-active.sync="showSidepanel"  md-persistent="full" >
      
             <!-- EDITION COMPONENT -->
                  <md-toolbar class="md-transparent" md-elevation="2">

                      <md-button class="md-icon-button md-dense" @click="toggleMenu" style="margin-left:auto">
                          <b-icon-x variant="danger" font-scale="7.5"></b-icon-x>                   
                       </md-button>
                  </md-toolbar>
                    <div style="padding: 1em"></div>
                  
                    <form style=" width: 85%;
                                  height: 85%;
                                margin-right: auto;
                                margin-left: auto; border: 1px solid blue" @submit.prevent="onSubmit">

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
      editions:Array,
      slug:String
  },
  components: {
    
    NewsEdition,
    BibliographyEdition,
    PrimaryTagsEdition,
    SecondaryTagsEdition,
    BIconX
    
  },

  data: () => ({
    showNavigation: false,
    showSidepanel: false,
    specificEdition:null,
    title: '',
    body:'',
    tags:[],
    bibliographyName: '',
    bibliographyLink:''
  }),

  methods:{
      toggleMenu(){
          this.showSidepanel =  !this.showSidepanel
          this.$emit('hide-panel')
      },
      newsChange(title,body){
        this.title = title
        this.body= body
        console.log(title)
        console.log(body)
      },
      primaryTagsEditionChange(primaryTags){
        this.tags = primaryTags
        console.log(primaryTags)
      },
      secondaryTagsEditionChange(secondaryTags){
        this.tags = secondaryTags
        console.log(secondaryTags)
      },
      bibliographyEditionChange(names,links){
        this.bibliographyName = names
        this.bibliographyLink = links

      },
      onSubmit() {
        // Tell the REST API to create a new edition for this news based on the user input, then update some data properties
        
        console.log('aqui voy a enviar una edition nueva')
        console.log(this.slug)
        console.log(this.tags)
        console.log('aqui va los tags')
        var i = 0
        var tagsAux = []
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
        console.log(tagsAux)

        var method = "";
       
        method = "POST"
         
        let endpoint = `/api/news/${this.slug}/edition/`;
        apiService(endpoint, method, { title: this.title,body: this.body, tags: tagsAux }).then(
          data => {
            console.log('este es la data que me entrego al responder la pregunta')
            console.log(data)
            this.editions.unshift(data);
            this.toggleMenu()
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
  },
  created(){
    console.log('se esta creando el drawer')
    this.showSidepanel = this.showPanel
    console.log(this.editions)
    console.log(this.tags)
    this.specificEdition = this.editions[0]
    if(this.specificEdition !== undefined){

          this.title = this.specificEdition.title
          this.body = this.specificEdition.body
          this.tags = this.specificEdition.tags
          this.bibliographyName = this.specificEdition.bibliography_name
          this.bibliographyLink = this.specificEdition.bibliography_link

    }
        console.log(this.tags)

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