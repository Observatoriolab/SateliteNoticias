<template>
  <!-- PRIMARY TAGS COMPONENT -->

  <div
    style="width: 90%;  margin-left:auto;margin-right:auto;text-align:center"
  >
    <h4 style="color: blue">Tags secundarios</h4>

    <b-row style="color: blue" fluid>
      <!--<vue-tags-input
        v-model="tag"
        :tags="tags"
        @tags-changed="newTags => (tags = newTags)"
        v-on:change="onChange"
      /> -->
      <multiselect @input="onChange"  v-model="value" tag-placeholder="Add this as new tag" placeholder="Search or add a tag" label="name" track-by="code" :options="options" :multiple="true" :taggable="true" @tag="addTag"></multiselect>
      
    </b-row>
  </div>
  <!-- PRIMARY TAGS COMPONENT -->
</template>
<script>
import Multiselect from 'vue-multiselect'

export default {
  name: "SecondaryTags",
  props: {
    secondaryTags: Array
  },
  components: {
      Multiselect
  },
  data() {
    return {
      tag: "",
      tags: [],
      value: [
      ],
      options: [
        //Los code deben corresponder para que funcione bien el componente
        { name: 'Vue.js', code: 'Vue.js' },
        { name: 'Javascript', code: 'Javascript' },
        { name: 'Open Source', code: 'Open Source' },
        { name: 'Vue.js2', code: 'Vue.js2' },
        { name: 'Javascript2', code: 'Javascript2' },
        { name: 'Open Source2', code: 'Open Source2' },

        { name: 'Vue.js3', code: 'Vue.js3' },
        { name: 'Javascript3', code: 'Javascript3' },
        { name: 'Open Source3', code: 'Open Source3' },

        { name: 'Vue.js4', code: 'Vue.js4' },
        { name: 'Javascript4', code: 'Javascript4' },
        { name: 'Open Source4', code: 'Open Source4' },
        { name: 'Vue.js5', code: 'Vue.js5' },
        { name: 'Javascript5', code: 'Javascript5' },
        { name: 'Open Source5', code: 'Open Source5' },
        { name: 'Vue.js6', code: 'Vue.js6' },
        { name: 'Javascript6', code: 'Javascript6' },
        { name: 'Open Source6', code: 'Open Source6' },
        { name: 'Open Source7', code: 'Open Source7' },
      ]
    
    };
  },

  methods: {

    onChange(){
       var aux = []
        for(var i=0;i<this.value.length;i++){
            aux.push(this.value[i].name)
        }
        this.$emit("secondary-tags-change", aux);

    },
    addTag (newTag) {
        const tag = {
          name: newTag,
          code: newTag
        }
        this.options.push(tag)
        this.value.push(tag)
        var aux = []
        for(var i=0;i<this.value.length;i++){
            aux.push(this.value.name)
        }
        this.$emit("secondary-tags-change", aux);

    }
  },
  created() {
    var i = 0;
    for (i = 0; i < this.secondaryTags.length; i++) {
      this.$set(this.value, i, { name: this.$props.secondaryTags[i], code:this.$props.secondaryTags[i]});
    }
  }
};
</script>
<style scoped>
.vue-tags-input {
  max-width: none;
  width: 100%;
}
</style>
