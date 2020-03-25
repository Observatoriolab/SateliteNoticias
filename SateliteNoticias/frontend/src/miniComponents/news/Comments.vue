<template>
    <div style="width:50%; margin-right:auto;margin-left:auto;padding:0.8em 0.8em 0.8em 0.8em ">
      <form  @submit.prevent="onSubmit"> 
          <b-row>
                    <div class="float:left">
                        <h4 class="text-primary p-2">Comentarios</h4>

                  </div>

                  <div class="float:right">
                        <b-button type="submit" variant="success" >
                        Postear
                      </b-button>


                  </div>
              
            </b-row>
         
            <b-form-textarea
                    id="textarea"
                    placeholder="Escribe tu comentario aqui!"
                    rows="3"
                    max-rows="12"
                    v-model="newCommentBody"
                  >
                  
            </b-form-textarea>



      </form>
  
  

          <div style="padding: 1em"></div>

                    <vue-custom-scrollbar class="scroll-area" v-bind:style="{position: 'relative',
                                                                  margin: 'auto',
                                                                  
                                                                  width: '100%',
                                                                  height: '20em' }"
                                                              :settings="settings" 
                                                            >
                              <div :key="updateComments" > 


                                      <ul class="list-unstyled" >
                                        <b-media v-for="comment in comments" :key="comment.key">

                                          <template v-slot:aside>
                                            <b-img blank blank-color="#abc" width="64" alt="placeholder"></b-img>
                                          </template>
                                          <h5 class="mt-1 mb-1">      
                                            {{comment.author}}
                                            
                                            
                                          </h5>
                                          <p class="mb-0">
                                            {{comment.body}}

                                          </p>
                                            <div style="padding: 1em"></div>

                                        </b-media>

                                      </ul>
                            </div>

                  </vue-custom-scrollbar>
      
           <b-row >

                <b-col md="5">

                

                </b-col>
                  <b-col md="4">
                      <div style="padding:1em"></div>
                      <b-button
                            v-show="next"
                            @click="getNewsComments"
                            variant="success"
                            :disabled=disableButton()
                          >
                        Load More
                      </b-button>

                </b-col>
                  <b-col md="3">


                </b-col>
              

        </b-row>

</div>
</template>
<script>
import vueCustomScrollbar from 'vue-custom-scrollbar'
import { apiService } from "@/common/api.service.js";
import _ from 'lodash'

export default {
    name:"Comments",
    props: {
        slug:String
    },
     data() {
          return {
            settings: {
                     maxScrollbarLength: 20
            },
            comments: [],
            next:null,
            newCommentBody: null,
            requestUser:null,
            updateComments:0,
            pageNumbers:[],
            updatedComments:[],
            disableFlag:false,
            lastPage:null,
            count:0,
            delayTime: 1000

          }
      },
    components: {
        vueCustomScrollbar
    },
    watch: {
       // whenever comments changes, this function will run
         comments: function (newComments, oldComments) {
              //console.log('se cambiaron las noticias o.o')
              console.log(newComments,oldComments)
          }
          
    },
    beforeUpdate(){
              this.debouncedGetComments()

    },
    methods: {
          disableButton(){
              return this.disableFlag
          },
          setRequestUser() {
              // the username has been set to localStorage by the App.vue component
              this.requestUser = window.localStorage.getItem("username");
          },
          async delayedComments(item) {        
                await apiService(item).then(data => {
                  //console.log('este es la data')
                  //console.log(data.results)
                  this.updatedComments.push(...data.results);
                  return data.results
                  

                });
          },
          async getcomments() {
            //console.log(this.pageNumbers)

            for (const [idx, url] of this.pageNumbers.entries()) {
              console.log(url)
              const todo = await this.delayedComments(url);
              console.log(`Received Todo ${idx+1}:`, todo);
            }
            console.log(this.updatedComments)
            for(var i=0;i<this.updatedComments.length;i++){
              console.log(this.updatedComments[i])
              this.$set(this.comments,i,this.updatedComments[i])
            }
            this.updatedComments.splice(0)
            
            this.updateComments +=1
            console.log('Done updating the comments!');


          },
           getLastDigit(pageString,optional){
                let regex = /=+\d*/.exec(pageString)
                console.log(regex[0])
                var nuevo = /\d+$/.exec(regex[0])
                console.log(nuevo[0])
                console.log(parseInt(nuevo[0])-1+optional)
                return (parseInt(nuevo[0])-1+optional).toString()

          },
          async getNewsComments() {
              // get a page of comments for a single news from the REST API's paginated 'news Endpoint'
              this.disableFlag = true
               var muchTime = window.performance.now()
                var muchTimeDate = new Date().getTime();
                var endpoint = `/api/news/${this.slug}/comments/`;
                if (this.next) {
                  endpoint = this.next;
                }
                console.log(this.next)
                await apiService(endpoint).then(data => {data
                  this.comments.push(...data.results);
                  console.log('esto es lo que salio')
                  console.log(data)
                  console.log(this.next)

                  if(data.results.length === 0){
                    this.pageNumbers.push("/api/news/"+this.slug+"/comments/?page=1")

                  }
                  else if (data.next) {
                    this.next = data.next;
                    console.log('este es el next')
                    console.log(this.next)
                    this.pageNumbers.push("/api/news/"+this.slug+"/comments/?page="+this.getLastDigit(this.next,0))

                  }
                  else {
                    console.log(this.next)
                    console.log("sadness ensuess")
                    this.next = endpoint
                    this.pageNumbers.push("/api/news/"+this.slug+"/comments/?page="+this.getLastDigit(endpoint,1))
                    this.next = null
                    this.count = data.count

                  }
                    console.log(this.pageNumbers)

                  var muchTime2 = window.performance.now()
                  var muchTimeDate2 = new Date().getTime();
                  console.log("Call to doSomething took " + (muchTime2 - muchTime) + " milliseconds.");
                  console.log("Call to doSomething took " + (muchTimeDate2 - muchTimeDate) + " milliseconds.");
                  this.delayTime +=500
                  this.disableFlag = false
                });
          },
          async onSubmit() {        
              if (this.newCommentBody) {
                let endpoint = `/api/news/${this.slug}/comment/`;
                await apiService(endpoint, "POST", { body: this.newCommentBody}).then(
                  data => {
                    console.log('este es la data que me entrego al responder la pregunta')
                    console.log(data)
                    //Hay que ver si se tiene que agregar una pagina mas
                    console.log(this.count)
                    this.count +=1
                    if(this.count % 4 === 1 && this.count > 4){
                      console.log('pase por aca pue')
                         this.pageNumbers.push("/api/news/"+this.slug+"/comments/?page="+parseInt(Math.floor(this.count/4)+1))
                         this.delayTime +=500

                    }
                  
                  }
                );
                this.newCommentBody = null;
                if (this.error) {
                  this.error = null;
                }
              } else {
                this.error = "You can't send an empty comment!";
              }
          }
    },
    created() {

      console.log(this.slug)
      this.getNewsComments();
      this.setRequestUser();
      this.debouncedGetComments = _.debounce(this.getcomments, this.delayTime)

  }
}
</script>
<style scoped>

</style>