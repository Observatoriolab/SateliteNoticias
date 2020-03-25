<template>
  <b-container style="text-align:center" fluid>
    <!-- BANNER COMPONENT -->
    <Banner></Banner>
    <!-- BANNER COMPONENT -->
    <!-- WHOLE COMPONENT -->
    <div style="padding-top: 1em"></div>

    <h3 style="color: blue">{{ $route.params.newsPiece.title }}</h3>

    <b-row>
      <b-col md="5">
        <NewsSummaryFull
          :fullContent="$route.params.fullContent"
        ></NewsSummaryFull>
      </b-col>

      <b-col md="7">
        <Edition
          :slug="$route.params.slug"
          :showPanel="true"
          @hide-panel="hidePanel"
          :mode="false"
        ></Edition>
      </b-col>
    </b-row>
    <b-row>
      <Comments :slug="$route.params.slug"></Comments>
    </b-row>
  </b-container>
</template>

<script>
import Banner from "@/miniComponents/main/Banner.vue";

import Edition from "./Edition.vue";

import Comments from "@/miniComponents/news/Comments.vue";
import NewsSummaryFull from "@/miniComponents/news/NewsSummaryFull.vue";
import { apiService } from "@/common/api.service.js";

export default {
  name: "fullNews",
  props: {
    fullContent: String,
    slug: String,
    mode: Boolean,
    newsPiece: Object
  },
  components: {
    Banner,
    Edition,
    Comments,
    NewsSummaryFull
  },
  data() {
    return {};
  },
  watch: {},
  methods: {
     hidePanel(bibliographyName, bibliographyLink, slug, tags) {

      if (slug.length !== 0) {
        this.editnews(bibliographyName, bibliographyLink, slug, tags);
      }
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
    console.log(this.$route.params.newsPiece.title);
  }
};
</script>
<style scoped></style>
