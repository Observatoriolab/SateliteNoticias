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
        <vue-single-select
          v-model="bibliographyNameModelSelect"
          :options="bibliographyNameArray"
          :getOptionValue="nameSelected"
          :inputId="'asdsad'"
        ></vue-single-select>

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
export default {
  name: "Bibliography",
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
    bibliographyLinkArray: []
  }),
  methods: {
    addBibliography() {
      //console.log('paso por aqui')
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
      //console.log(this.bibliographyNameArray)
      //console.log(this.bibliographyLinkArray)

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
      //console.log('esto es lo que me entro')
      //console.log(this.bibliographyName)
      //console.log(this.bibliographyLink)
      if (this.bibliographyName.length !== 0) {
        var nameArray = this.bibliographyName.split(";");
        var linkArray = this.bibliographyLink.split(";");
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
    createStrings() {
      //console.log('estos son los arrays para irme')
      //console.log(this.bibliographyNameArray[0])
      //console.log(this.bibliographyLinkArray)
      for (var i = 0; i < this.bibliographyNameArray.length; i++) {
        this.bibliographyNameInternal =
          this.bibliographyNameInternal + this.bibliographyNameArray[i] + ";";
        //console.log(this.bibliographyNameInternal)
        this.bibliographyLinkInternal =
          this.bibliographyLinkInternal + this.bibliographyLinkArray[i] + ";";
      }
      //console.log('ASI SALIERON')
      //console.log(this.bibliographyNameInternal)
      //console.log(this.bibliographyLinkInternal)
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
    //console.log(this.bibliographyNameModelSelect)
    if (this.bibliographyNameModelSelect === null) {
      this.bibliographyLinkModelSelect = "";
    }
  }
};
</script>
<style lang="stylus"></style>
