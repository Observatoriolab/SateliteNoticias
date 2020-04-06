<template>
  <!-- PRIMARY TAGS COMPONENT -->

  <div style="width: 96%;  margin-left:auto;margin-right:auto">
    <b-row style="color: blue;border: 1px solid blue; text-align:center;" fluid>
      <b-col md="4">
        <h6>EJE</h6>
       <multiselect  v-model="value" :selectLabel="''"  placeholder="value" label="name" track-by="name"></multiselect>

      </b-col>

      <b-col md="4">


        <h6>PAIS/REGION</h6>
                <multiselect    v-model="value2" :selectLabel="''"  placeholder="Selecciona uno" label="name" track-by="name"></multiselect>


      </b-col>

      <b-col md="4">
        <h6>ORGANISMO</h6>
            <multiselect   v-model="value3" :selectLabel="''"  placeholder="Selecciona uno" label="name" track-by="name"></multiselect>

      </b-col>

    </b-row>
  </div>

  <!-- PRIMARY TAGS COMPONENT -->
</template>
<script>
import Multiselect from 'vue-multiselect'

export default {
  name: "PrimaryTags",
  props: {
    first: String,
    second: String,
    third: String,
    tags: Array,
    tags2: Array,
    tags3: Array
  },
  components: {
    Multiselect
  },

  data() {
    return {
    value: { name: '', code: ''},
    options: [

    ],
     value2: { name: '', code: ''},
    options2: [

    ],
     value3: { name: '', code: ''},
    options3: [

    ],


    };
  },
  methods: {
  
    createArrays() {
      var nameArray = this.tagsInternal.split(";");
      var nameArray2 = this.tagsInternal2.split(";");
      var nameArray3 = this.tagsInternal3.split(";");

      for (var i = 0; i < nameArray.length - 1; i++) {
        this.$set(this.options, i, {name:nameArray[i], code:nameArray[i]});
      }

      for (i = 0; i < nameArray2.length - 1; i++) {
        this.$set(this.options2, i, {name:nameArray[i], code:nameArray[i]});
      }

      for (i = 0; i < nameArray3.length - 1; i++) {
        this.$set(this.options3, i, {name:nameArray[i], code:nameArray[i]});
      }
     },
   
  },

  created() {
    /*this.value.name=this.first
    this.value.code=this.first

    this.value.name=this.second
    this.value.code=this.second

    this.value.name=this.third
    this.value.code=this.third
    */
/*  this.tagsInternal = this.tags;
    this.tagsInternal2 = this.tags2;
    this.tagsInternal3 = this.tags3;
  */
    //this.createArrays()

  }
};
</script>
<style lang="stylus"></style>
