<template>
  <!-- EDITION COMPONENT -->
  <b-col md="3" class="p-2 bg-light">
    <div>
      <NewsEdition></NewsEdition>
      <PrimaryTagsEdition></PrimaryTagsEdition>
      <AddTagsEdition></AddTagsEdition>
      <BibliographyEdition></BibliographyEdition>
    </div>
  </b-col>
  <!-- EDITION COMPONENT -->
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
  }
};
</script>
<style lang="stylus"></style>