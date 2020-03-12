<template>

<div >
    
        <md-button @click="showSidepanel = true">Favorites</md-button>

          <md-drawer class="md-right" :md-active.sync="showSidepanel">
      
             <!-- EDITION COMPONENT -->
                    <div style="padding: 1em"></div>
                  
                    <div style=" width: 82%;
                                margin-right: auto;
                                margin-left: auto;">

                      <NewsEdition></NewsEdition>
                      <PrimaryTagsEdition></PrimaryTagsEdition>
                      <AddTagsEdition></AddTagsEdition>
                      <BibliographyEdition></BibliographyEdition>
                    </div>

                  
                  <!-- EDITION COMPONENT -->

           </md-drawer>
  </div>
 
</template>
<script>

import NewsEdition from "@/miniComponents/edition/NewsEdition.vue";
import BibliographyEdition from "@/miniComponents/edition/BibliographyEdition.vue";
import AddTagsEdition from "@/miniComponents/edition/AddTagsEdition.vue";
import PrimaryTagsEdition from "@/miniComponents/edition/PrimaryTagsEdition.vue";

export default {
  name: "Edition",
  components: {
    
    NewsEdition,
    BibliographyEdition,
    AddTagsEdition,
    PrimaryTagsEdition
    
  },
    data: () => ({
      showNavigation: false,
      showSidepanel: false
    })
};
</script>
<style scoped>
 .page-container {
    min-height: 300px;
    overflow: hidden;
    position: relative;
    border: 1px solid rgba(#000, .12);
  }

  .md-drawer {
    width: 35%;
    max-width: 100vw;
  }

  .md-content {
    padding: 16px;
  }

</style>