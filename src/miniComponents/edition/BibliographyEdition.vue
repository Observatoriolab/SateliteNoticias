<template>
  <div style="text-align:center">
    <h4 style="padding:1em;  color:blue">Bibliografia</h4>

    <b-row
      style="width: 95%; text-align:center;  margin-left:auto;margin-right:auto;  color:blue"
      fluid
    >

      <b-col md="3">
        <h6>Nombre:</h6>
        <div style="padding:0.5em"></div>
        <h6>Link:</h6>
      </b-col>

      <b-col md="9">
        <multiselect  :tagPlaceholder="'Enter agrega'" @input="nameSelected" :taggable="true" @tag="addTag" v-model="value" :selectLabel="'Enter selecciona'" :options="options" placeholder="Selecciona o agrega uno" label="name" track-by="name"></multiselect>
        <div style="padding:0.2em"></div>

        <b-form-input @update="updateWarning" v-model="bibliographyLinkModelSelect"> </b-form-input>
        <h6 v-show="warning" style="color:red">Porfavor agrege el link correspondiente</h6>
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
    value: { name: '', code: ''},
    options: [

    ],
    warning:false
  }),
  methods: {   
    updateWarning(value){
      if (value.length !== 0) this.warning=false
    },
    addBibliography() {
      this.createStrings()
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
          this.$set(this.options, i, {name:nameArray[i], code:nameArray[i]});
          this.$set(this.bibliographyLinkArray, i, linkArray[i]);
        }
      }
    },
    createStrings() {
      for (var i = 0; i < this.options.length; i++) {
        this.bibliographyNameInternal =
          this.bibliographyNameInternal + this.options[i].name + ";";
        this.bibliographyLinkInternal =
          this.bibliographyLinkInternal + this.bibliographyLinkArray[i] + ";";
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
    addTag (newTag) {
        const tag = {
          name: newTag,
          code: newTag
        }
        console.log('Este es el nuevo tag')
        console.log(newTag)
        console.log(tag)
        if(this.bibliographyLinkModelSelect.length !== 0){

            this.options.push(tag)
            this.bibliographyLinkArray.push(this.bibliographyLinkModelSelect)
            this.bibliographyLinkModelSelect = ''
            this.addBibliography()
        }
        else{
          this.warning = true
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
