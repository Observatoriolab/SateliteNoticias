<template>
  <div
    style=" width: 90%; margin-left:auto; margin-right:auto; text-align:center;"
  >
      <h4 style="color: blue">Tags primarios</h4>

    <b-row>
      <b-col md="4">
        <h6>EJE</h6>
       <multiselect  :taggable="true" @tag="addTag" v-model="value" :selectLabel="''" :options="options" :placeholder="value" label="name" track-by="name"></multiselect>

      </b-col>

      <b-col md="4">


        <h6>PAIS/REGION</h6>
                <multiselect :taggable="true" @tag="addTag2"  v-model="value2" :selectLabel="''" :options="options2" placeholder="Selecciona uno" label="name" track-by="name"></multiselect>


      </b-col>

      <b-col md="4">
        <h6>ORGANISMO</h6>
            <multiselect  :taggable="true" @tag="addTag3" v-model="value3" :selectLabel="''" :options="options3" placeholder="Selecciona uno" label="name" track-by="name"></multiselect>

      </b-col>

    </b-row>
  </div>
</template>
<script>
import Multiselect from 'vue-multiselect'
//TODO: SE TIENE QUE AGREGAR LA FECHA
export default {
  name: "PrimaryTagsEdition",
  props: {
    tags: Array,
    tags2: Array,
    tags3: Array
  },
  components: {
    Multiselect
  },

  data: () => ({
    tagsInternal: null,
    tagsInternal2: null,
    tagsInternal3:null,
    bibliographyNameInternal:'',
    bibliographyNameInternal2:'',
    bibliographyNameInternal3:'',
    value: { name: '', code: ''},
    options: [

    ],
     value2: { name: '', code: ''},
    options2: [

    ],
     value3: { name: '', code: ''},
    options3: [

    ],
  }),

  methods: {
     addPrimaryTags() {
      this.createStrings()
      this.$emit(
        "primarytags-change",
        this.bibliographyNameInternal,
        this.bibliographyNameInternal2,
        this.bibliographyNameInternal3
      );
    },
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
    createStrings() {
      var i;
      for ( i = 0; i < this.options.length; i++) {
        this.bibliographyNameInternal =
          this.bibliographyNameInternal + this.options[i].name + ";";
      }
      for (i = 0; i < this.options2.length; i++) {
        this.bibliographyNameInternal2 =
          this.bibliographyNameInternal2 + this.options2[i].name + ";";
      }
      for ( i = 0; i < this.options3.length; i++) {
        this.bibliographyNameInternal3 =
          this.bibliographyNameInternal3 + this.options3[i].name + ";";
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

        this.options.push(tag)

    },
        addTag2 (newTag) {
        const tag = {
          name: newTag,
          code: newTag
        }
        console.log('Este es el nuevo tag')
        console.log(newTag)
        console.log(tag)

        this.options2.push(tag)

    },
        addTag3 (newTag) {
        const tag = {
          name: newTag,
          code: newTag
        }
        console.log('Este es el nuevo tag')
        console.log(newTag)
        console.log(tag)

        this.options3.push(tag)

    },
  },

  created() {
    this.tagsInternal = this.tags;
    this.tagsInternal2 = this.tags2;
    this.tagsInternal3 = this.tags3;
    //this.createArrays()

  }
};
</script>
<style scope>
.buttonn {
  border: 1px solid white;
}
</style>
