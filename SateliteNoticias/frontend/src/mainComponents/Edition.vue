<template>

<div >
    

          <md-drawer class="md-right" :md-active.sync="showSidepanel"  md-persistent="full" >
      
             <!-- EDITION COMPONENT -->
                  <md-toolbar class="md-transparent" md-elevation="2">

                      <md-button class="md-icon-button md-dense" @click="toggleMenu" style="margin-left:auto">
                          <b-icon-x variant="danger" font-scale="7.5"></b-icon-x>                   
                       </md-button>
                  </md-toolbar>
                    <div style="padding: 1em"></div>
                  
                    <form style=" width: 85%;
                                  height: 85%;
                                margin-right: auto;
                                margin-left: auto; border: 1px solid blue">

                      <NewsEdition></NewsEdition>
                                          <div style="padding: 1em"></div>

                      <PrimaryTagsEdition></PrimaryTagsEdition>
                                          <div style="padding: 1em"></div>

                      <SecondaryTagsEdition></SecondaryTagsEdition>
                                          <div style="padding: 1em"></div>

                      <BibliographyEdition></BibliographyEdition>
                      <PublishButton></PublishButton>
                    </form>

                  
                  <!-- EDITION COMPONENT -->

           </md-drawer>
  </div>
 
</template>
<script>

import NewsEdition from "@/miniComponents/edition/NewsEdition.vue";
import BibliographyEdition from "@/miniComponents/edition/BibliographyEdition.vue";
import PrimaryTagsEdition from "@/miniComponents/edition/PrimaryTagsEdition.vue";
import SecondaryTagsEdition from "@/miniComponents/edition/SecondaryTagsEdition.vue";
import PublishButton from  "@/miniComponents/edition/PublishButton.vue";

import { BIconX } from 'bootstrap-vue'


export default {
  name: "Edition",
  props:{
      showPanel:Boolean
  },
  components: {
    
    NewsEdition,
    BibliographyEdition,
    PrimaryTagsEdition,
    SecondaryTagsEdition,
    PublishButton,
    BIconX
    
  },

  data: () => ({
    showNavigation: false,
    showSidepanel: false
  }),

  methods:{
      toggleMenu(){
            this.showSidepanel =  !this.showSidepanel

      }
  },
  created(){
    console.log('se esta creando el drawer')
    this.showSidepanel = this.showPanel
  },
  beforeUpdate(){
    console.log('se viene')
    console.log('se destruye')
    this.showSidepanel = false
    this.$emit('hide-panel')
  }
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