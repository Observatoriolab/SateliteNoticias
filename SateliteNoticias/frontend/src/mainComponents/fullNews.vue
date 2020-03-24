<template>
    <b-container style="text-align:center" fluid >
    <!-- BANNER COMPONENT -->
    <Banner></Banner>
    <!-- BANNER COMPONENT -->
        <!-- WHOLE COMPONENT -->
                                    <div style="padding-top: 1em"></div>

    <h3 style="color: blue">  {{$route.params.newsPiece.title}}</h3>

    <b-row>
        <b-col md="5" >
            <NewsSummaryFull :fullContent="$route.params.fullContent"></NewsSummaryFull>
        </b-col>

        <b-col md="7" >

            <Edition :slug="$route.params.slug" :showPanel="true" @hide-panel="hidePanel" :mode="false"></Edition>
            
        </b-col>
            
    </b-row>
    <b-row >

        <Comments :slug="$route.params.slug" ></Comments>


    </b-row>

    </b-container>
</template>

<script>
import Banner from "@/miniComponents/main/Banner.vue";

import Edition from "./Edition.vue";

import Comments from "@/miniComponents/news/Comments.vue";
import NewsSummaryFull from "@/miniComponents/news/NewsSummaryFull.vue";

export default {
    name: 'fullNews',
    props:{
        fullContent:String,
        slug:String,
        mode:Boolean,
        newsPiece:Object
    },
    components: {
        Banner,
        Edition,
        Comments,
        NewsSummaryFull
        
    },
    data() {
        return {
        
        }
    },
    watch: {


    },
    methods:{
        hidePanel(){

        }
   
    },
    created() {
        console.log(this.$route.params.newsPiece.title)
    }
    
}
</script>
<style scoped>

</style>