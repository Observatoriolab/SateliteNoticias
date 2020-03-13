<template>
  <!-- NEWS COMPONENT -->

   <vue-custom-scrollbar class="scroll-area" :settings="settings" 
                          v-bind:style="{position: relative,
                                        margin: auto,                                                          
                                        width: '100%',
                                        height: '60em' }">


          <b-col md="12" >
               
                
                    <NewsSummary></NewsSummary>

                    <PrimaryTags></PrimaryTags>
                    <SecondaryTags></SecondaryTags>

                    <Bibliography></Bibliography>

                    <RelevanceEdition></RelevanceEdition>


            
          </b-col>
          <!-- NEWS COMPONENT -->

  </vue-custom-scrollbar>

</template>
<script>
import NewsSummary from "@/miniComponents/news/NewsSummary.vue";
import PrimaryTags from "@/miniComponents/news/PrimaryTags.vue";
import SecondaryTags from "@/miniComponents/news/SecondaryTags.vue";

import Bibliography from "@/miniComponents/news/Bibliography.vue";
import RelevanceEdition from "@/miniComponents/news/RelevanceEdition.vue";
import vueCustomScrollbar from 'vue-custom-scrollbar'

export default {
  name: "News",
  data() {
    return {
      settings: {
        maxScrollbarLength: 100
      }
    }
  },
  components: {
    NewsSummary,
    PrimaryTags,
    Bibliography,
    RelevanceEdition,
    vueCustomScrollbar,
    SecondaryTags

  },
  methods: {
    scrollHandle(evt) {
      console.log(evt)
    }
  }
};
</script>
<style scoped>
</style>