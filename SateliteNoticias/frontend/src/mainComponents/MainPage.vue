<template>
  <b-container fluid>
    <!-- BANNER COMPONENT -->

    <Banner></Banner>

    <!-- BANNER COMPONENT -->

    <!-- WHOLE COMPONENT -->
    <b-row align-h="start">
      <!-- CATEGORY COMPONENT -->

      <b-col md="2">
        <Categories @clicked-category="categoryClicked"></Categories>
      </b-col>
      <!-- CATEGORY COMPONENT -->

      <b-col md="7">
        <!-- SEARCH BUTTONS COMPONENT -->

        <SearchButtons></SearchButtons>
        <!-- SEARCH BUTTONS COMPONENT -->
        <vue-custom-scrollbar
          class="scroll-area"
          :settings="settings"
          v-bind:style="{ textAlign: 'center', width: '100%', height: '40em' }"
        >
          <b-row>
            <div>
              <div
                v-for="(newsPiece, index) in news"
                v-bind:key="newsPiece.key"
              >
                <News
                  @clicked-edition="clickedEdition"
                  :llave="index"
                  :title="newsPiece.title"
                  :link="newsPiece.link"
                  :content="newsPiece.content"
                  :primaryTags="newsPiece.primaryTags"
                  :secondaryTags="newsPiece.tags"
                  :bibliography_name="newsPiece.bibliography_name"
                  :bibliography_link="newsPiece.bibliography_link"
                  :relevance="newsPiece.relevance"
                  :irrelevance="newsPiece.irrelevance"
                  :slug="newsPiece.slug"
                  :fullContent="newsPiece.fullContent"
                  :newsPiece="newsPiece"
                  :updateNews="updateNews"
                >
                </News>
              </div>
            </div>
          </b-row>
        </vue-custom-scrollbar>

        <b-row align-h="center">
          <div class="button p-5">
            <b-button
              v-show="next"
              @click="getnewsLoadMore"
              variant="success"
              :disabled="disableButton()"
            >
              Load More
            </b-button>
          </div>
        </b-row>
      </b-col>

      <div v-if="editionToggle">
        <Edition
          :slug="slug"
          :showPanel="editionToggle"
          @hide-panel="hidePanel"
          :mode="true"
        ></Edition>
      </div>
    </b-row>
    <!-- WHOLE COMPONENT -->
  </b-container> </template
>>
<script>
import Banner from "@/miniComponents/main/Banner.vue";
import Categories from "@/miniComponents/main/Categories.vue";
import SearchButtons from "@/miniComponents/main/SearchButtons.vue";
import News from "./News.vue";
import vueCustomScrollbar from "vue-custom-scrollbar";
import { apiService } from "@/common/api.service.js";
import Edition from "./Edition.vue";
import _ from "lodash";
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
      next: null,
      filterFlag: false,
      pageCount: null,
      settings: {
        maxScrollbarLength: 20
      },
      categoryToFilterWith: null,
      editionToggle: false,
      editions: [],
      slug: "",
      endpoint: "/api/news/",
      pageNumbers: [],
      updateNews: 0,
      updateFullNews: 0,
      updateEditions: 0,
      disableFlag: false,
      delayTime: 9700
    };
  },
  watch: {
    // whenever question changes, this function will run
    news: function(newNews, oldNews) {
      //console.log('se cambiaron las noticias o.o')
      console.log(newNews, oldNews);
    }
  },

  beforeUpdate() {
    console.log("El tiempo de delay ahora es de: " + this.delayTime.toString());
    this.debouncedGetNews();
  },

  methods: {
    disableButton() {
      return this.disableFlag;
    },
    categoryClicked(category) {
      this.categoryToFilterWith = category;
      //Llamada a la API para filtrar con este tag mas grande

      let endpoint = `/api/news/tags/${this.categoryToFilterWith}/`;
      let method = "GET";
      apiService(endpoint, method).then(data => {
        //console.log("este es el resultado de lo que me dio el back")
        //console.log(data.results)
        this.news = data.results;
        this.filterFlag = true;
        this.next = null;
      });
    },
    //Se apreto el boton de editar por lo que se debe desplegar el drawer derecho para ver/editar la edicion
    clickedEdition(slug) {
      this.slug = slug;
      this.editionToggle = true;
    },

    hidePanel(bibliographyName, bibliographyLink, slug, tags) {
      console.log(this.editionToggle);

      this.editionToggle = false;
      if (slug.length !== 0) {
        this.editnews(bibliographyName, bibliographyLink, slug, tags);
      }
    },

    async delayedNews(item) {
      await apiService(item).then(data => {
        //console.log('este es la data')
        //console.log(data.results)
        this.updatedNews.push(...data.results);
        return data.results;
      });
    },
    async getnews() {
      //console.log(this.pageNumbers)

      for (const [idx, url] of this.pageNumbers.entries()) {
        console.log(url);
        const todo = await this.delayedNews(url);
        console.log(`Received Todo ${idx + 1}:`, todo);
      }
      console.log(this.updatedNews);
      for (var i = 0; i < this.updatedNews.length; i++) {
        console.log(this.updatedNews[i]);
        this.$set(this.news, i, this.updatedNews[i]);
      }
      this.updatedNews.splice(0);

      this.updateNews += 1;
      console.log("Done updating the news!");
    },
    getLastDigit(pageString) {
      let regex = /=+\d*/.exec(pageString);
      console.log(regex[0]);
      var nuevo = /\d+$/.exec(regex[0]);
      console.log(nuevo);
      return parseInt(nuevo[0]) - 1;
    },
    async getnewsLoadMore() {
      this.disableFlag = true;

      this.loadingnews = true;
      //console.log(this.news)

      if (this.next) {
        this.endpoint = this.next;
      }
      var muchTime = window.performance.now();
      var muchTimeDate = new Date().getTime();
      await apiService(this.endpoint).then(data => {
        this.news.push(...data.results);
        console.log(data);
        this.loadingnews = false;
        if (data.next) {
          this.next = data.next;
          this.pageNumbers.push(
            "/api/news/?page=" + this.getLastDigit(this.next)
          );
        } else {
          this.next = null;
        }
        var muchTime2 = window.performance.now();
        var muchTimeDate2 = new Date().getTime();
        console.log(
          "Call to doSomething took " +
            (muchTime2 - muchTime) +
            " milliseconds."
        );
        console.log(
          "Call to doSomething took " +
            (muchTimeDate2 - muchTimeDate) +
            " milliseconds."
        );
        this.delayTime += 300;
        this.disableFlag = false;
      });
    },

    editnews(bibliographyName, bibliographyLink, slug, tags) {
      let endpoint = "/api/news/" + slug + "/";
      //console.log('este son los tags')
      //console.log(tags)
      let method = "PUT";
      console.log("estos son los tags");
      console.log(tags);
      var tagsAux = [];
      console.log(tags);
      console.log(tags.length);
      if (tags[0].text !== undefined) {
        for (var i = 0; i < tags.length; i++) {
          this.$set(tagsAux, i, tags[i].text);
        }
      } else {
        for (var j = 0; j < tags.length; j++) {
          this.$set(tagsAux, j, tags[j]);
        }
      }
      apiService(endpoint, method, {
        tags: tagsAux,
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
    document.title = "Satelite de Noticias";

    //console.log('estas son las news')
    //console.log(this.news);
    this.debouncedGetNews = _.debounce(this.getnews, this.delayTime);
  }
};
</script>
<style scoped></style>>
