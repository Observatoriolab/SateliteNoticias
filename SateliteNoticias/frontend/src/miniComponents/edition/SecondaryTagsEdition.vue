<template>
    <!-- PRIMARY TAGS COMPONENT -->

    <div style="width: 90%;  margin-left:auto;margin-right:auto;text-align:center">
          <h4 style="color: blue">Tags secundarios</h4>

          <b-row style="color: blue" fluid>

                      <vue-tags-input
                        v-model="tag"
                        :tags="tags"
                        @tags-changed="newTags => tags = newTags"
                      />
                      
                   
            </b-row>

      
    </div>
            


  

    
    <!-- PRIMARY TAGS COMPONENT -->
</template>
<script>
import VueTagsInput from '@johmun/vue-tags-input';

export default {
  name: "SecondaryTags",
  components:{
VueTagsInput
  },
  data() {
    return {
      tag: '',
      tags: [],
    };
  },
};
</script>
<style scoped>

.vue-tags-input {
  max-width: none;
  width: 100%;
}

</style>