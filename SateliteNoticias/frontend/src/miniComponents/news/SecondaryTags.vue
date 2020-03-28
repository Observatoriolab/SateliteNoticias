<template>
  <!-- PRIMARY TAGS COMPONENT -->

  <div :key="updateNews" style="width: 96%;  margin-left:auto;margin-right:auto;text-align:center">
    <b-row style="color: blue;border: 1px solid blue; justify-content:center" fluid>
      <h5 style="padding: 0.5em 0.5em 0em 0.5em; float:right">Tags secundarios</h5>
      <!--<vue-tags-input
        v-model="tag"
        :tags="tags"
        @tags-changed="newTags => (tags = newTags)"
      />
      -->
        <multiselect  :disabled="true" v-model="value" tag-placeholder="Add this as new tag" placeholder="Search or add a tag" label="name" track-by="code" :options="options" :multiple="true" :taggable="true" @tag="addTag"></multiselect>

    </b-row>
  </div>

  <!-- PRIMARY TAGS COMPONENT -->
</template>
<script>
//import VueTagsInput from "@johmun/vue-tags-input";
import Multiselect from 'vue-multiselect'

export default {
  name: "SecondaryTags",
  props: {
    secondaryTags: Array,
    updateNews: Number
  },
  components: {
 //   VueTagsInput,
    Multiselect
  
  },
  data() {
    return {
      tag: "",
      tags: [],
       value: [
      ],
      options: [
        { name: 'Vue.js', code: 'vu' },
        { name: 'Javascript', code: 'js' },
        { name: 'Open Source', code: 'os' },
        { name: 'Vue.js2', code: 'vu2' },
        { name: 'Javascript2', code: 'js2' },
        { name: 'Open Source2', code: 'os2' },

        { name: 'Vue.js3', code: 'vu3' },
        { name: 'Javascript3', code: 'js3' },
        { name: 'Open Source3', code: 'os3' },

        { name: 'Vue.js4', code: 'vu4' },
        { name: 'Javascript4', code: 'js4' },
        { name: 'Open Source4', code: 'os4' },
        { name: 'Vue.js5', code: 'vu5' },
        { name: 'Javascript5', code: 'js5' },
        { name: 'Open Source5', code: 'os5' },
        { name: 'Vue.js6', code: 'vu6' },
        { name: 'Javascript6', code: 'js6' },
        { name: 'Open Source6', code: 'os6' },
        { name: 'Open Source7', code: 'os7' },
      ]
    };
  },
  methods:{
    addTag (newTag) {
      const tag = {
        name: newTag,
        code: newTag
      }
      this.options.push(tag)
      this.value.push(tag)
    }
  },
  created() {
    console.log(this.$props.secondaryTags)
    var i = 0;
    for (i = 0; i < this.$props.secondaryTags.length; i++) {
      this.$set(this.value, i, { name: this.$props.secondaryTags[i], code:this.$props.secondaryTags[i]});
    }
    //console.log(this.tags)
  },
   beforeUpdate() {
    console.log("llego algo");
    console.log(this.updateNews);
    console.log(this.secondaryTags);
    for (var i = 0; i < this.$props.secondaryTags.length; i++) {
      this.$set(this.value, i, { name: this.$props.secondaryTags[i], code:this.$props.secondaryTags[i]});
    }
  }
};
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css">
</style>