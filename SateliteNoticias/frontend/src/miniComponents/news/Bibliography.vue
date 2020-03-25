<template>
  <b-row
    style="width: 100%; text-align:center;  margin-left:auto;margin-right:auto; border:1px solid blue; color:blue; "
    fluid
    :key="updateNews"
  >
    <b-row>
      <div style="padding-left:3em"></div>
      <h4 class="text-primary" style="text-align:center">Bibliografia</h4>
    </b-row>
    <b-row style="margin-left:auto;margin-right:auto; ">
      <b-col md="5">
        <h6>Nombre:</h6>

        <vue-single-select
          v-model="bibliographyNameModelSelect"
          :options="bibliographyNameArray"
          :getOptionValue="nameSelected"
          :inputId="'id' + slug + content + title"
        ></vue-single-select>
      </b-col>
      <b-col md="2"></b-col>
      <b-col md="5">
        <h6>Link:</h6>
        <b-form-input v-model="bibliographyLinkModelSelect"> </b-form-input>
      </b-col>
    </b-row>
  </b-row>
</template>
<script>
export default {
  name: "Bibliography",
  props: {
    bibliography_name: String,
    bibliography_link: String,
    slug: String,
    content: String,
    title: String,
    updateNews: Number
  },
  data: () => ({
    bibliographyNameModelSelect: "",
    bibliographyNameArray: [],
    bibliographyLinkModelSelect: "",
    bibliographyLinkArray: []
  }),
  methods: {
    createArrays() {
      //console.log('esto es lo que me entro')
      //console.log(this.bibliography_name)
      //console.log(this.bibliography_link)
      if (this.bibliography_name.length !== 0) {
        var nameArray = this.bibliography_name.split(";");
        var linkArray = this.bibliography_link.split(";");
        //console.log(nameArray)
        //console.log(linkArray)
        //console.log(nameArray.length-1)
        //console.log(linkArray.length)
        for (var i = 0; i < nameArray.length - 1; i++) {
          this.$set(this.bibliographyNameArray, i, nameArray[i]);
          this.$set(this.bibliographyLinkArray, i, linkArray[i]);
        }
      }
    },
    nameSelected(parameter) {
      //console.log('paso por aqui2')
      //console.log(parameter)

      var pos = this.bibliographyNameArray.lastIndexOf(parameter);
      this.bibliographyLinkModelSelect = this.bibliographyLinkArray[pos];
    }
  },
  created() {
    this.createArrays();
  },
  beforeUpdate() {
    console.log("llego algo");
    console.log(this.updateNews);
    console.log(this.bibliography_name);
    this.createArrays();
    if (this.bibliographyNameModelSelect === null) {
      this.bibliographyLinkModelSelect = "";
    }
  }
};
</script>
<style lang="stylus"></style>
