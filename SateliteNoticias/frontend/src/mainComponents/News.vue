<template>
  <!-- NEWS COMPONENT -->

 

          <b-col md="11" style="margin-left:auto;margin-right:auto" >
               
                  <div style="padding: 2em"></div>
                    <NewsSummary></NewsSummary>

                    <PrimaryTags></PrimaryTags>
                    <SecondaryTags></SecondaryTags>

                    <Bibliography></Bibliography>

                    <RelevanceEdition @clicked-edition="clickedEdition"></RelevanceEdition>
                    <NewsSummaryFull></NewsSummaryFull>
                    <Comments></Comments>


            
          </b-col>
          <!-- NEWS COMPONENT -->


</template>
<script>
import NewsSummary from "@/miniComponents/news/NewsSummary.vue";
import PrimaryTags from "@/miniComponents/news/PrimaryTags.vue";
import SecondaryTags from "@/miniComponents/news/SecondaryTags.vue";

import Bibliography from "@/miniComponents/news/Bibliography.vue";
import RelevanceEdition from "@/miniComponents/news/RelevanceEdition.vue";
import Comments from "@/miniComponents/news/Comments.vue";
import NewsSummaryFull from "@/miniComponents/news/NewsSummaryFull.vue";


export default {
  name: "News",
  data() {
    return {
    }
  },
  components: {
    NewsSummary,
    PrimaryTags,
    Bibliography,
    RelevanceEdition,
    SecondaryTags,
    Comments,
    NewsSummaryFull

  },
  methods: {
    clickedEdition() {
        this.$emit('clicked-edition')
    }
  }
};
</script>
<style scoped>
</style>