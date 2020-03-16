<template>
  <!-- NEWS COMPONENT -->

 

          <b-col md="11" style="margin-left:auto;margin-right:auto" >
               
                  <div style="padding: 2em"></div>
                    <NewsSummary :openOrClosed="openOrClosed" @clicked-fullNews="fullNewsClicked"></NewsSummary>

                    <PrimaryTags></PrimaryTags>
                    <SecondaryTags></SecondaryTags>

                    <Bibliography></Bibliography>

                    <RelevanceEdition @clicked-edition="clickedEdition"></RelevanceEdition>

                    <div v-if="fullNewsToggle">

                        <NewsSummaryFull></NewsSummaryFull>
                        <Comments></Comments>


                    </div>

            
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
      fullNewsToggle: false,
      openOrClosed: false
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
    },
    fullNewsClicked(toggle) {
      console.log('aqui se apreto el seguir leyendo')
      if(toggle){
          this.fullNewsToggle = true
          this.openOrClosed = true

      }
      else{
          this.fullNewsToggle = false
          this.openOrClosed = false

      }
    }
  }
};
</script>
<style scoped>
</style>