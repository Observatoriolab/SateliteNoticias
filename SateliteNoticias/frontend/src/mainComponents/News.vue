<template>
  <!-- NEWS COMPONENT -->

 

          <b-col md="11" style="margin-left:auto;margin-right:auto" >
               
                  <div style="padding: 2em"></div>
                    <NewsSummary 
                              :title="title"
                              :content="content"
                              :link="link"
                          :openOrClosed="openOrClosed" 
                          
                          
                          @clicked-fullNews="fullNewsClicked"
                    
                    ></NewsSummary>

                    <PrimaryTags 
                                 :primaryTags="primaryTags"
                    >

                    </PrimaryTags>
                    <SecondaryTags 
                            :secondaryTags="secondaryTags"
                    >


                    </SecondaryTags>

                    <Bibliography
                          :bibliography="bibliography"

                    >


                    </Bibliography>

                    <RelevanceEdition 
                               @clicked-edition="clickedEdition"
                                :relevance="relevance"
                                :irrelevance="irrelevance"
                               
                               >
                          
                    
                    </RelevanceEdition>

                    <div v-if="fullNewsToggle">

                        <NewsSummaryFull
                           :fullContent="fullContent"
                        >
                        
                        </NewsSummaryFull>


                        <Comments
                            :slug="slug"

                        >
                        
                        
                        </Comments>


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
  props:{
          title:String,
          content:String,
          visits:Number,
          fullContent:String,
          primaryTags:Array,
          secondaryTags:Array,
          bibliography: Object,
          relevance: Number,
          irrelevance:Number,
          link: String,
          slug: String

  },
  data() {
    return {
      fullNewsToggle: false,
      openOrClosed: false,
      comments: [],
      next:null
      
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
  created(){
    console.log('aqui va algo 2')
    console.log(this.$props)
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