<template>
    <!-- PRIMARY TAGS COMPONENT -->

    <div style="width: 90%;  margin-left:auto;margin-right:auto;text-align:center">
          <h4 style="color: blue">Tags secundarios</h4>

          <b-row style="color: blue" fluid>

                      <vue-tags-input
                        v-model="tag"
                        :tags="tags"
                        @tags-changed="newTags => tags = newTags"
                        v-on:change="onChange"
                      />
                      
                   
            </b-row>

      
    </div>
            


  

    
    <!-- PRIMARY TAGS COMPONENT -->
</template>
<script>
import VueTagsInput from '@johmun/vue-tags-input';

export default {
  name: "SecondaryTags",
  props:{
    secondaryTags:Array
  },
  components:{
        VueTagsInput
  },
  data() {
    return {
      tag: '',
      tags: []
    };
  },
  
  methods:{
      onChange(){
        this.$emit('secondary-tags-change', this.tags)
      }
  },
  updated(){
        this.onChange();

  },
  created(){
    //console.log('aqui va los tags')
    //console.log(this.secondaryTags)
    var i = 0
    for(i=0;i<this.secondaryTags.length;i++){
          this.$set(this.tags, i, {"text":this.secondaryTags[i]})

    }
    //console.log(this.tags)
  }
};
</script>
<style scoped>

.vue-tags-input {
  max-width: none;
  width: 100%;
}

</style>