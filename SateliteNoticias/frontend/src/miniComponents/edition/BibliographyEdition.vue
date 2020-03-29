<template>
  <div style="text-align:center">
    <h4 style="padding:1em;  color:blue">Bibliografia</h4>

    <b-row
      style="width: 95%; text-align:center;  margin-left:auto;margin-right:auto;  color:blue"
      fluid
    >
      <b-col md="2 p-2">
        <h6>Nombre:</h6>
        <div style="padding:0.5em"></div>
        <h6>Link:</h6>
      </b-col>

      <b-col md="4">
      <!--  <vue-single-select
          v-model="bibliographyNameModelSelect"
          :options="bibliographyNameArray"
          :getOptionValue="nameSelected"
          :inputId="'asdsad'"
        ></vue-single-select>
      -->
        <multiselect   :taggable="true" @tag="addTag" v-model="value" :options="options" :custom-label="nameWithLang" placeholder="Select one" label="name" track-by="name"></multiselect>

        <b-form-input v-model="bibliographyLinkModelSelect"> </b-form-input>
      </b-col>

      <b-col md="2 p-2">
        <h6>Nombre:</h6>
        <div style="padding:0.5em"></div>
        <h6>Link:</h6>
      </b-col>

      <b-col md="3">
        <b-form-input v-model="bibliographyNameModel"> </b-form-input>
        <div style="padding:0.2em"></div>

        <b-form-input v-model="bibliographyLinkModel"> </b-form-input>
      </b-col>

      <b-col md="1">
        <div class="button">
          <b-button @click="addBibliography" circled lg="4" variant="primary"
            >+</b-button
          >
        </div>
      </b-col>
    </b-row>
  </div>
</template>
<script>
import Multiselect from 'vue-multiselect'

export default {
  name: "Bibliography",
  components: {
    Multiselect
  },
  props: {
    bibliographyName: String,
    bibliographyLink: String
  },
  data: () => ({
    bibliographyNameInternal: "",
    bibliographyLinkInternal: "",
    bibliographyNameModel: "",
    bibliographyNameModelSelect: "",
    bibliographyNameArray: [],
    bibliographyLinkModel: "",
    bibliographyLinkModelSelect: "",
    bibliographyLinkArray: [],
    value: { name: 'Vue.js', language: 'JavaScript' },
    options: [
      { name: 'Vue.js', language: 'JavaScript' },
      { name: 'Rails', language: 'Ruby' },
      { name: 'Sinatra', language: 'Ruby' },
      { name: 'Laravel', language: 'PHP' },
      { name: 'Phoenix', language: 'Elixir' }
    ]
  }),
  methods: {
    nameWithLang ({ name }) {
      return `${name}`
    },
    addBibliography() {
      this.$set(
        this.bibliographyNameArray,
        this.bibliographyNameArray.length,
        this.bibliographyNameModel
      );
      this.$set(
        this.bibliographyLinkArray,
        this.bibliographyLinkArray.length,
        this.bibliographyLinkModel
      );
      console.log('paso para aqui')
      console.log(this.bibliographyNameInternal)
      console.log(this.bibliographyLinkInternal)

      this.createStrings();
      this.bibliographyLinkModel = "";
      this.bibliographyNameModel = "";
      
      this.$emit(
        "bibliography-change",
        this.bibliographyNameInternal,
        this.bibliographyLinkInternal
      );
    },
    createArrays() {
      if (this.bibliographyName.length !== 0) {
        var nameArray = this.bibliographyName.split(";");
        var linkArray = this.bibliographyLink.split(";");
 
        for (var i = 0; i < nameArray.length - 1; i++) {
          this.$set(this.bibliographyNameArray, i, nameArray[i]);
          this.$set(this.bibliographyLinkArray, i, linkArray[i]);
        }
      }
    },
    createStrings() {
      for (var i = 0; i < this.bibliographyNameArray.length; i++) {
        this.bibliographyNameInternal =
          this.bibliographyNameInternal + this.bibliographyNameArray[i] + ";";
        this.bibliographyLinkInternal =
          this.bibliographyLinkInternal + this.bibliographyLinkArray[i] + ";";
      }
    },
    nameSelected(parameter) {

      var pos = this.bibliographyNameArray.lastIndexOf(parameter);
      this.bibliographyLinkModelSelect = this.bibliographyLinkArray[pos];
    },
    addTag (newTag) {
        const tag = {
          name: newTag,
          language: newTag
        }
        this.options.push(tag)
        this.value.push(tag)
        var aux = []
        for(var i=0;i<this.value.length;i++){
            aux.push(this.value.name)
        }

    }
  },
  created() {
    this.createArrays();
  },
  beforeUpdate() {
    if (this.bibliographyNameModelSelect === null) {
      this.bibliographyLinkModelSelect = "";
    }
  }

};
</script>
<style lang="stylus"></style>
