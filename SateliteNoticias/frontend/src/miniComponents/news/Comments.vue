<template>
    <div style="width:50%; margin-right:auto;margin-left:auto;padding:0.8em 0.8em 0.8em 0.8em ">
      <b-row>
              <b-col md="10">
                  <h4 class="text-primary p-2">Comentarios</h4>

             </b-col>

             <b-col md="2">
                  <b-button type="submit" variant="success" >
                  Postear
                </b-button>


             </b-col>
        
      </b-row>
         
            <b-form-textarea
                    id="textarea"
                    placeholder="Escribe tu comentario aqui!"
                    rows="3"
                    max-rows="12"
                    v-model="newCommentBody"
                  >
                  
            </b-form-textarea>
  

          <div style="padding: 1em"></div>
        <vue-custom-scrollbar class="scroll-area" v-bind:style="{position: 'relative',
                                                          margin: 'auto',
                                                          
                                                          width: '100%',
                                                          height: '20em' }"
                                                      :settings="settings" 
                                                     >


                        <ul class="list-unstyled">
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
            requestUser:null

          }
      },
    components: {
        vueCustomScrollbar
    },
    methods: {
          setRequestUser() {
              // the username has been set to localStorage by the App.vue component
              this.requestUser = window.localStorage.getItem("username");
          },
          getNewsComments() {
          // get a page of comments for a single news from the REST API's paginated 'news Endpoint'
                let endpoint = `/api/news/${this.slug}/comments/`;
                if (this.next) {
                  endpoint = this.next;
                }
                apiService(endpoint).then(data => {
                  this.comments.push(...data.results);
                  //console.log('estos son las respuestas')
                  //console.log(data.results)
                  //console.log(data.next)
                  if (data.next) {
                    this.next = data.next;
                  } else {
                    this.next = null;
                  }
                });
        },
        onSubmit() {
          // Tell the REST API to create a new edition for this news based on the user input, then update some data properties
          
            //console.log('aqui voy a enviar una respuesta nueva')
            //console.log(this.slug)
            //console.log(this.new)
            if (this.newCommentBody) {
              let endpoint = `/api/news/${this.slug}/comment/`;
              apiService(endpoint, "POST", { body: this.newCommentBody}).then(
                data => {
                  //console.log('este es la data que me entrego al responder la pregunta')
                  //console.log(data)
                  this.comments.unshift(data);
                }
              );
              this.newCommentBody = null;
              this.showForm = false;
              this.userHasEditioned = true;
              if (this.error) {
                this.error = null;
              }
            } else {
              this.error = "You can't send an empty comment!";
            }
        }
    },
    created() {
        this.getNewsComments();
        this.setRequestUser();
  }
}
</script>
<style scoped>

</style>