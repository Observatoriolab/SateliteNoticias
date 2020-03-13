<template>
    <!-- PRIMARY TAGS COMPONENT -->

    <div style="width: 90%;  margin-left:auto;margin-right:auto;">

          <b-row style="color: blue;text-align:center" fluid>

                    <h5 style="padding: 0.5em 0.5em 0em 0.5em;" >Tags secundarios</h5>
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