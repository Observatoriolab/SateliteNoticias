<template>
  <!-- NEWS COMPONENT -->

  <b-col md="10" style="margin-left:auto; margin-right:auto">
    <div style="padding: 2em"></div>
    <NewsSummary
      :title="title"
      :content="content"
      :link="link"
      :openOrClosed="openOrClosed"
      :slug="slug"
      :fullContent="fullContent"
      :newsPiece="newsPiece"
      
    ></NewsSummary>

    <PrimaryTags :primaryTags="primaryTags"> </PrimaryTags>
    <SecondaryTags :secondaryTags="secondaryTags" 
      :updateNews="updateNews"> </SecondaryTags>

    <Bibliography
      :bibliography_name="bibliography_name"
      :bibliography_link="bibliography_link"
      :slug="slug"
      :content="content"
      :title="title"
      :updateNews="updateNews"
    >
    </Bibliography>

    <RelevanceEdition
      @clicked-edition="clickedEdition"
      :newsPiece="newsPiece"
      :slug="slug"
      :updateNews="updateNews"
    >
    </RelevanceEdition>
  </b-col>

  <!-- NEWS COMPONENT -->
</template>
<script>
import NewsSummary from "@/miniComponents/news/NewsSummary.vue";
import PrimaryTags from "@/miniComponents/news/PrimaryTags.vue";
import SecondaryTags from "@/miniComponents/news/SecondaryTags.vue";

import Bibliography from "@/miniComponents/news/Bibliography.vue";
import RelevanceEdition from "@/miniComponents/news/RelevanceEdition.vue";

export default {
  name: "News",
  props: {
    title: String,
    content: String,
    visits: Number,
    primaryTags: Array,
    secondaryTags: Array,
    bibliography_name: String,
    bibliography_link: String,
    relevance: Number,
    irrelevance: Number,
    link: String,
    slug: String,
    fullNewsToggle: Boolean,
    llave: Number,
    fullContent: String,
    newsPiece: Object,
    updateNews: Number
  },
  data() {
    return {
      openOrClosed: false,
      comments: [],
      next: null,
      next2: null,
      updateEdition: 0
    };
  },
  components: {
    NewsSummary,
    PrimaryTags,
    Bibliography,
    RelevanceEdition,
    SecondaryTags
  },
  methods: {
    clickedEdition() {
      //console.log('estos son las ediciones')
      //console.log(this.editions)
      this.$emit("clicked-edition", this.slug);
    }
  },
  created() {
    console.log(this.newsPiece);
  }
};
</script>
<style scoped></style>
