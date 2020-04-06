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
        <multiselect  @input="nameSelected" v-model="value" :selectLabel="'Enter selecciona'" :options="options" placeholder="Selecciona uno" label="name" track-by="name"></multiselect>
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
import Multiselect from 'vue-multiselect'

export default {
  name: "Bibliography",
    components: {
    Multiselect
  },
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
    bibliographyLinkArray: [],
    value: { name: '', code: ''},
    options: [

    ],
  }),
  methods: {
    createArrays() {
      if (this.bibliography_name.length !== 0) {
        var nameArray = this.bibliography_name.split(";");
        var linkArray = this.bibliography_link.split(";");
        for (var i = 0; i < nameArray.length - 1; i++) {
          this.$set(this.options, i, {name:nameArray[i], code:nameArray[i]});
          this.$set(this.bibliographyLinkArray, i, linkArray[i]);
        }
      }
    },
      nameSelected(parameter) {
      console.log('hola como va')
      console.log(parameter)
      if(parameter !== null){
        var arrNames = this.options.map(el => el.name);
        var pos = arrNames.lastIndexOf(parameter.name);
        this.bibliographyLinkModelSelect = this.bibliographyLinkArray[pos];
      }
      else{
        this.bibliographyLinkModelSelect = ''
      }
    },

  },
  created() {
    this.createArrays();
  },
  beforeUpdate() {
    this.createArrays();
    if (this.bibliographyNameModelSelect === null) {
      this.bibliographyLinkModelSelect = "";
    }
  }
};
</script>
<style lang="stylus"></style>
