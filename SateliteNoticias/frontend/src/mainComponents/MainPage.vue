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

                        <div :key="updateNews">
                          
                                <div v-for="newsPiece in news" v-bind:key="newsPiece.key">


                                          <News   @clicked-edition="clickedEdition"
                                                  @update-edition="UpdateEdition"
                                                  :title="newsPiece.title"
                                                  :link="newsPiece.link"
                                                  :content="newsPiece.content"
                                                  :fullContent="newsPiece.fullContent"
                                                  :primaryTags="newsPiece.primaryTags"
                                                  :secondaryTags="newsPiece.tags"
                                                  :bibliography_name="newsPiece.bibliography_name"
                                                  :bibliography_link="newsPiece.bibliography_link"
                                                  :relevance="newsPiece.relevance"
                                                  :irrelevance="newsPiece.irrelevance"
                                                  :slug="newsPiece.slug"
                                          
                                          
                                          >

                                            



                                          </News>

                          

                                    </div>

                          
                          
                            </div>
                      






                </vue-custom-scrollbar>
             

            </b-row>

          </b-col>


          <div v-if="editionToggle"> 
                   <Edition :slug="slug" :showPanel="editionToggle" @hide-panel="hidePanel"></Edition>

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
                @click="getnewsLoadMore"
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
      updatedNews: [],
      next:null,
      filterFlag: false,
      pageCount: null,
      settings: {
        maxScrollbarLength: 20
      },
      categoryToFilterWith: null,
      editionToggle: false,
      editions: [],
      slug:'',
      endpoint: "/api/news/",
      pageNumbers:[],
      updateNews: 0,
      updateEditions: 0
    }
  },
   watch: {
    // whenever question changes, this function will run
    news: function (newNews, oldNews) {
      //console.log('se cambiaron las noticias o.o')
      console.log(newNews,oldNews)
      this.debouncedGetNews()
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
            //console.log("este es el resultado de lo que me dio el back")
            //console.log(data.results)
            this.news = data.results
            this.filterFlag = true
            this.next = null
        });

    },
    //Se apreto el boton de editar por lo que se debe desplegar el drawer derecho para ver/editar la edicion
    clickedEdition(slug){      
        this.slug = slug
        this.editionToggle = true
    },
    UpdateEdition(ediciones){
        //console.log(ediciones)

            for(var i=0;i<ediciones.length;i++){
                this.$set(this.editions,i,ediciones[i])
            }
        
    },
    hidePanel(bibliographyName,bibliographyLink,slug,tags){
       console.log(this.editionToggle)

        this.editionToggle = false
        if(slug.length !== 0){
            this.editnews(bibliographyName,bibliographyLink,slug,tags)

        }
    },

    async delayedNews(item) {        
          apiService(item).then(data => {
            //console.log('este es la data')
            //console.log(data.results)
            this.updatedNews.push(...data.results);
            return data.results
            

          });
    },
   
    async getnews() {
      //console.log(this.pageNumbers)

      for (const [idx, url] of this.pageNumbers.entries()) {
        console.log(url)
        const todo = await this.delayedNews(url);
        console.log(`Received Todo ${idx+1}:`, todo);
      }
      for(var i=0;i<this.updatedNews.length;i++){
        console.log(this.updatedNews[i])
        this.$set(this.news,i,this.updatedNews[i])
      }
      this.updatedNews.splice(0)
      this.updateNews +=1
      //console.log('Done updating the news!');


    },
    getLastDigit(pageString){
        return parseInt(pageString.substr(pageString.length-1))-1

    },
    async getnewsLoadMore() {
   
      this.loadingnews = true;
      //console.log(this.news)

      if(this.next){
        this.endpoint = this.next
      }

      await apiService(this.endpoint).then(data => {
        this.news.push(...data.results);
        //console.log(data)
        this.loadingnews = false;
        if (data.next) {
          this.next = data.next
          this.pageNumbers.push("/api/news/?page="+this.getLastDigit(this.next))
        } else {
          this.next = null;

        }
      });
    },

    editnews(bibliographyName,bibliographyLink,slug,tags) {
      
        let endpoint = "/api/news/"+slug+"/";
        //console.log('este son los tags')
        //console.log(tags)
        let method = "PUT"
        console.log('estos son los tags')
        console.log(tags)
        apiService(endpoint, method, {
           tags:tags,
           bibliography_name: bibliographyName, 
           bibliography_link: bibliographyLink
        }).then(news_data => {
          console.log("esta es la data que me dio en el front");
          console.log(news_data);
        });
      }
  },
  created() {
    this.getnewsLoadMore();

    //console.log('estas son las news')
    //console.log(this.news);
    this.debouncedGetNews = _.debounce(this.getnews, 10000)
    document.title = "Satelite de Noticias";
  }
};
</script>
<style scoped>

</style>>