<template>
      <div >
      
          <div style="padding: 7px"></div>
          <div style="color: blue;border:1px solid blue;font-size: 15px; text-align:center">
                   
                      <h2 style="color: blue">Cuerpo de la noticia</h2>

              <!--TODO: DISABLE DEL SCROLL DE LAS NOTICIAS PARA PODER SCROLLEAR EL CONTENIDO SIN PROBLEMAS 
                        CONDICIONES: ESTAR EN HOVER EN EL ELEMENTO
              -->

                     <vue-custom-scrollbar class="scroll-area" v-bind:style="{position: 'relative',
                                                          margin: 'auto',
                                                          
                                                          width: '100%',
                                                          height: '30em' }"
                                                      :settings="settings" 
                                                     >
                          <p style="padding: 1em; 0em; 1em; 1em" >
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at risus diam. Quisque ac sem at sem tempus luctus non a magna. Sed pretium sit amet velit non rhoncus. In congue vitae ipsum tempor dictum. Mauris malesuada ornare justo, fringilla semper risus porttitor id. Ut id velit sem. In lacinia, odio congue ornare facilisis, arcu elit facilisis augue, vel luctus diam sem vitae mi. Suspendisse faucibus neque in risus sodales mollis. Proin sit amet tincidunt arcu. Cras ultrices ultricies auctor. Nullam vestibulum scelerisque condimentum. Cras euismod enim dolor, eu sollicitudin magna blandit sed. Mauris faucibus sit amet nulla sed elementum. Suspendisse id velit tellus. Fusce ultrices turpis in tellus bibendum, eget convallis dui sagittis. Duis at porttitor lacus.

                            Sed mattis mi lobortis arcu feugiat, eu faucibus urna mollis. Curabitur hendrerit placerat libero eu placerat. Sed eget nisi a diam imperdiet porttitor. Ut nisi sapien, aliquam in egestas a, blandit sit amet risus. Mauris ornare lacus sed mauris vulputate iaculis. Nam at magna in lectus gravida lobortis ut et mauris. Fusce massa nunc, imperdiet sit amet tristique eu, sagittis in nunc. Pellentesque vitae elit sed libero lacinia commodo et vitae eros. Praesent vulputate, mauris porta interdum consectetur, arcu nisi malesuada nibh, quis commodo risus magna sit amet arcu. Sed iaculis ante lacus, ac finibus orci malesuada sit amet. Vivamus feugiat erat velit, non cursus est mollis nec.

                            Morbi sit amet consectetur lorem. Nullam accumsan urna ex, at convallis justo vestibulum a. Morbi pulvinar arcu sit amet eleifend dapibus. Curabitur sodales tempus volutpat. Praesent quis ex id nunc pretium condimentum sed a odio. Fusce pulvinar ornare posuere. Aenean sit amet metus odio. Suspendisse mollis ultricies ultrices. Suspendisse potenti. Nullam at ipsum iaculis, blandit libero id, semper nunc. Sed urna eros, vulputate a blandit eu, mattis et urna. Maecenas eu rutrum leo.

                            Nunc fermentum eleifend leo ac viverra. Aliquam erat volutpat. Donec lobortis lobortis neque. Praesent congue eros quis sem vestibulum, eget sollicitudin risus imperdiet. Donec accumsan hendrerit odio, sed auctor lorem pretium ac. Curabitur tristique erat at dictum lobortis. Sed cursus massa vel est rhoncus, vitae tempus eros rhoncus. Suspendisse lobortis convallis lacus eget faucibus. Integer tristique tellus ultrices justo fringilla semper. Quisque sollicitudin, tortor in consequat molestie, urna lectus consectetur quam, eget maximus ex quam eget ex. Vestibulum nisl mauris, rhoncus sit amet lacus id, euismod dignissim tellus. Pellentesque sed interdum nibh.

                            Nulla facilisi. Nam accumsan lacus eget rhoncus aliquam. Ut lobortis ut sem at congue. Morbi mollis, eros non sodales ullamcorper, velit nisl tempus mauris, eu tincidunt tortor ex a nisi. Proin non metus elit. Integer condimentum neque sit amet dolor posuere, vel sollicitudin turpis rutrum. Vestibulum pharetra condimentum tortor, quis pulvinar sapien mattis et. In rutrum volutpat turpis, dignissim consequat libero lacinia ac. Donec ac eros id purus semper lacinia. Aliquam rhoncus enim vitae rhoncus molestie.
                          
                              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at risus diam. Quisque ac sem at sem tempus luctus non a magna. Sed pretium sit amet velit non rhoncus. In congue vitae ipsum tempor dictum. Mauris malesuada ornare justo, fringilla semper risus porttitor id. Ut id velit sem. In lacinia, odio congue ornare facilisis, arcu elit facilisis augue, vel luctus diam sem vitae mi. Suspendisse faucibus neque in risus sodales mollis. Proin sit amet tincidunt arcu. Cras ultrices ultricies auctor. Nullam vestibulum scelerisque condimentum. Cras euismod enim dolor, eu sollicitudin magna blandit sed. Mauris faucibus sit amet nulla sed elementum. Suspendisse id velit tellus. Fusce ultrices turpis in tellus bibendum, eget convallis dui sagittis. Duis at porttitor lacus.

                            Sed mattis mi lobortis arcu feugiat, eu faucibus urna mollis. Curabitur hendrerit placerat libero eu placerat. Sed eget nisi a diam imperdiet porttitor. Ut nisi sapien, aliquam in egestas a, blandit sit amet risus. Mauris ornare lacus sed mauris vulputate iaculis. Nam at magna in lectus gravida lobortis ut et mauris. Fusce massa nunc, imperdiet sit amet tristique eu, sagittis in nunc. Pellentesque vitae elit sed libero lacinia commodo et vitae eros. Praesent vulputate, mauris porta interdum consectetur, arcu nisi malesuada nibh, quis commodo risus magna sit amet arcu. Sed iaculis ante lacus, ac finibus orci malesuada sit amet. Vivamus feugiat erat velit, non cursus est mollis nec.

                            Morbi sit amet consectetur lorem. Nullam accumsan urna ex, at convallis justo vestibulum a. Morbi pulvinar arcu sit amet eleifend dapibus. Curabitur sodales tempus volutpat. Praesent quis ex id nunc pretium condimentum sed a odio. Fusce pulvinar ornare posuere. Aenean sit amet metus odio. Suspendisse mollis ultricies ultrices. Suspendisse potenti. Nullam at ipsum iaculis, blandit libero id, semper nunc. Sed urna eros, vulputate a blandit eu, mattis et urna. Maecenas eu rutrum leo.

                            Nunc fermentum eleifend leo ac viverra. Aliquam erat volutpat. Donec lobortis lobortis neque. Praesent congue eros quis sem vestibulum, eget sollicitudin risus imperdiet. Donec accumsan hendrerit odio, sed auctor lorem pretium ac. Curabitur tristique erat at dictum lobortis. Sed cursus massa vel est rhoncus, vitae tempus eros rhoncus. Suspendisse lobortis convallis lacus eget faucibus. Integer tristique tellus ultrices justo fringilla semper. Quisque sollicitudin, tortor in consequat molestie, urna lectus consectetur quam, eget maximus ex quam eget ex. Vestibulum nisl mauris, rhoncus sit amet lacus id, euismod dignissim tellus. Pellentesque sed interdum nibh.

                            Nulla facilisi. Nam accumsan lacus eget rhoncus aliquam. Ut lobortis ut sem at congue. Morbi mollis, eros non sodales ullamcorper, velit nisl tempus mauris, eu tincidunt tortor ex a nisi. Proin non metus elit. Integer condimentum neque sit amet dolor posuere, vel sollicitudin turpis rutrum. Vestibulum pharetra condimentum tortor, quis pulvinar sapien mattis et. In rutrum volutpat turpis, dignissim consequat libero lacinia ac. Donec ac eros id purus semper lacinia. Aliquam rhoncus enim vitae rhoncus molestie.
                         

                             Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at risus diam. Quisque ac sem at sem tempus luctus non a magna. Sed pretium sit amet velit non rhoncus. In congue vitae ipsum tempor dictum. Mauris malesuada ornare justo, fringilla semper risus porttitor id. Ut id velit sem. In lacinia, odio congue ornare facilisis, arcu elit facilisis augue, vel luctus diam sem vitae mi. Suspendisse faucibus neque in risus sodales mollis. Proin sit amet tincidunt arcu. Cras ultrices ultricies auctor. Nullam vestibulum scelerisque condimentum. Cras euismod enim dolor, eu sollicitudin magna blandit sed. Mauris faucibus sit amet nulla sed elementum. Suspendisse id velit tellus. Fusce ultrices turpis in tellus bibendum, eget convallis dui sagittis. Duis at porttitor lacus.

                            Sed mattis mi lobortis arcu feugiat, eu faucibus urna mollis. Curabitur hendrerit placerat libero eu placerat. Sed eget nisi a diam imperdiet porttitor. Ut nisi sapien, aliquam in egestas a, blandit sit amet risus. Mauris ornare lacus sed mauris vulputate iaculis. Nam at magna in lectus gravida lobortis ut et mauris. Fusce massa nunc, imperdiet sit amet tristique eu, sagittis in nunc. Pellentesque vitae elit sed libero lacinia commodo et vitae eros. Praesent vulputate, mauris porta interdum consectetur, arcu nisi malesuada nibh, quis commodo risus magna sit amet arcu. Sed iaculis ante lacus, ac finibus orci malesuada sit amet. Vivamus feugiat erat velit, non cursus est mollis nec.

                            Morbi sit amet consectetur lorem. Nullam accumsan urna ex, at convallis justo vestibulum a. Morbi pulvinar arcu sit amet eleifend dapibus. Curabitur sodales tempus volutpat. Praesent quis ex id nunc pretium condimentum sed a odio. Fusce pulvinar ornare posuere. Aenean sit amet metus odio. Suspendisse mollis ultricies ultrices. Suspendisse potenti. Nullam at ipsum iaculis, blandit libero id, semper nunc. Sed urna eros, vulputate a blandit eu, mattis et urna. Maecenas eu rutrum leo.

                            Nunc fermentum eleifend leo ac viverra. Aliquam erat volutpat. Donec lobortis lobortis neque. Praesent congue eros quis sem vestibulum, eget sollicitudin risus imperdiet. Donec accumsan hendrerit odio, sed auctor lorem pretium ac. Curabitur tristique erat at dictum lobortis. Sed cursus massa vel est rhoncus, vitae tempus eros rhoncus. Suspendisse lobortis convallis lacus eget faucibus. Integer tristique tellus ultrices justo fringilla semper. Quisque sollicitudin, tortor in consequat molestie, urna lectus consectetur quam, eget maximus ex quam eget ex. Vestibulum nisl mauris, rhoncus sit amet lacus id, euismod dignissim tellus. Pellentesque sed interdum nibh.

                            Nulla facilisi. Nam accumsan lacus eget rhoncus aliquam. Ut lobortis ut sem at congue. Morbi mollis, eros non sodales ullamcorper, velit nisl tempus mauris, eu tincidunt tortor ex a nisi. Proin non metus elit. Integer condimentum neque sit amet dolor posuere, vel sollicitudin turpis rutrum. Vestibulum pharetra condimentum tortor, quis pulvinar sapien mattis et. In rutrum volutpat turpis, dignissim consequat libero lacinia ac. Donec ac eros id purus semper lacinia. Aliquam rhoncus enim vitae rhoncus molestie.
                         
                          
                          </p>
                    </vue-custom-scrollbar>
                              <div style="padding: 1em"></div>

          </div>

      </div>
</template>
<script>
import vueCustomScrollbar from 'vue-custom-scrollbar'

export default {
  name: "NewsSummaryFull",
  props:{
    fullContent:String
  },
  data() {
    return {
      settings: {
        maxScrollbarLength: 20
      }
    }
  },
  components: {
     vueCustomScrollbar

  },
};
</script>
<style scoped>

</style>