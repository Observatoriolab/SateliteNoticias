<template>
  <!-- NEWS COMPONENT -->

   <vue-custom-scrollbar class="scroll-area" v-bind:style="{position: relative,
                                                          margin: auto,
                                                          
                                                          width: '100%',
                                                          height: '60em' }"
                                                      :settings="settings" 
                                                      @ps-scroll-y="scrollHandle">


          <b-col md="12" >
            <div>
              <NewsSummary></NewsSummary>

                  <b-row>
                    <PrimaryTags></PrimaryTags>
                  </b-row>
                  <b-row>
                    <b-col md="12" class="p-5"></b-col>
                  </b-row>
                  <b-row>
                    <Bibliography></Bibliography>
                  </b-row>

                  <b-row>
                    <RelevanceEdition></RelevanceEdition>
                  </b-row>


            </div>
            
          </b-col>
          <!-- NEWS COMPONENT -->
              <NewsSummary></NewsSummary>
              <NewsSummary></NewsSummary>
              <NewsSummary></NewsSummary>
              <NewsSummary></NewsSummary>
              <NewsSummary></NewsSummary>
              <NewsSummary></NewsSummary>

  </vue-custom-scrollbar>

</template>
<script>
import NewsSummary from "@/miniComponents/news/NewsSummary.vue";
import PrimaryTags from "@/miniComponents/news/PrimaryTags.vue";
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
    vueCustomScrollbar

  },
  methods: {
    scrollHandle(evt) {
      console.log(evt)
    }
  }
};
</script>
<style scoped>
.scroll-area {

}
</style>