<template>
  <b-container fluid >
    <!-- BANNER COMPONENT -->
    <Banner></Banner>
    <!-- BANNER COMPONENT -->

        <!-- WHOLE COMPONENT -->
        <b-row>
          <!-- CATEGORY COMPONENT -->
          <Categories  @clicked-category="categoryClicked"></Categories>
          <!-- CATEGORY COMPONENT -->

          <b-col md="7">
            <!-- SEARCH BUTTONS COMPONENT -->
            <SearchButtons></SearchButtons>
            <!-- SEARCH BUTTONS COMPONENT -->

            <b-row >
                <vue-custom-scrollbar class="scroll-area" :settings="settings" 
                          v-bind:style="{position: 'relative',
                                        margin: 'auto',                                                          
                                        width: '120%',
                                        height: '60em' }">


                  <div v-for="newsPiece in news" v-bind:key="newsPiece.key">


                      <News  @clicked-edition="clickedEdition"
                      
                              :title="newsPiece.title"
                              :link="newsPiece.link"
                              :content="newsPiece.content"
                              :fullContent="newsPiece.fullContent"
                              :primaryTags="newsPiece.primaryTags"
                              :secondaryTags="newsPiece.tags"
                              :bibliography="newsPiece.bibliography"
                              :relevance="newsPiece.relevance"
                              :irrelevance="newsPiece.irrelevance"
                              :slug="newsPiece.slug"
                      
                      
                      >

                         



                      </News>

                 

                  </div>







                </vue-custom-scrollbar>
             

            </b-row>

          </b-col>
          <div v-if="editionToggle"> 

               <Edition :showPanel="editionToggle" @hide-panel="hidePanel"></Edition>

          </div>


        </b-row>
        
        <!-- WHOLE COMPONENT -->

        <b-row >

          <b-col md="5">

           

          </b-col>
             <b-col md="4">
                <div style="padding:1em"></div>
                <b-button
                v-show="next"
                @click="getnews"
                variant="success"
                    >
                  Load More
                </b-button>

          </b-col>
             <b-col md="3">


          </b-col>
        

        </b-row>
          
  </b-container>
</template>>
<script>
import Banner from "@/miniComponents/main/Banner.vue";
import Categories from "@/miniComponents/main/Categories.vue";
import SearchButtons from "@/miniComponents/main/SearchButtons.vue";
import News from "./News.vue";
import Edition from "./Edition.vue";
import vueCustomScrollbar from 'vue-custom-scrollbar'
import { apiService } from "@/common/api.service.js";

export default {
  name: "MainPage",
  components: {
    Banner,
    Categories,
    SearchButtons,
    News,
    Edition,
    vueCustomScrollbar
  },
  data() {
    return {
      news: [],
      next:null,
      filterFlag: false,
      pageCount: null,
      settings: {
        maxScrollbarLength: 20
      },
      categoryToFilterWith: null,
      editionToggle: false
    }
  },
  methods:{
    categoryClicked(category){
        this.categoryToFilterWith = category
        //Llamada a la API para filtrar con este tag mas grande

        let endpoint = `/api/news/tags/${this.categoryToFilterWith}/`;
        let method = "GET"
        apiService(endpoint,method)
          .then(data => {
            console.log("este es el resultado de lo que me dio el back")
            console.log(data.results)
            this.news = data.results
            this.filterFlag = true
            this.next = null
        });

    },
    //Se apreto el boton de editar por lo que se debe desplegar el drawer derecho para ver/editar la edicion
    clickedEdition(){
        console.log("acabo de apretar el boton")
        this.editionToggle = true
    },
    hidePanel(){
        this.editionToggle = false
    },
    getnews() {
      console.log('estos son las preguntas antes de consultar a la api')
      console.log(this.news)
      let endpoint = "/api/news/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingnews = true;
      console.log(this.news)
      apiService(endpoint).then(data => {
        this.news.push(...data.results);
        console.log(data)
        this.loadingnews = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    }
  },
  created() {
    this.getnews();
    console.log('estas son las news')
    console.log(this.news);
    document.title = "Satelite de Noticias";
  }
};
</script>
<style scoped>

</style>>