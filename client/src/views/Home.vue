<template lang='pug'>
Flex.dashboard(padding="20px", width="fill", height="fill")
  Flex(col, padding="0", :fixWidth="300", height="fill")
    Temp(temp='-16' city='Ульяновск')
    Block(title="Участки", width="fill", height="fill")
      Region(
        v-for='(region, i) in getRegions' 
        :region='region' :key='i'
        :active='selectRG === region.name'
        @click='selectedRG(region.name)'
      )
    Block(title="Техника", width="fill", height="fill")
      Snowplow(
        v-for='(snowplow, i) in getSnowplows' 
        :snowplow='snowplow' :key='i'
        :active='selectSP === snowplow.name'
        @click='selectedSP(snowplow.name)'
      )
    Block(title="Настройки", width="fill")
  Map(
    title="Карта",
     width="fill", 
     height="fill", 
     :lines="getLines" 
     :regions='getRegions' 
     :snowplows='getSnowplows'
     :selectRG='selectRG'
     :selectSP='selectSP'
     @selectedRG='selectedRG($event)'
     @selectedSP='selectedSP($event)'
     )
</template>

<script>
export default {
  name: "Home",
  data: () => {
    return {
      selectRG: null,
      selectSP: null
    }
  },
  components: {
    Block: () => import("@/components/templates/Block.vue"),
    Region: () => import("@/components/elements/Region.vue"),
    Snowplow: () => import("@/components/elements/Snowplow.vue"),
    Temp: () => import("@/components/blocks/Temp.vue"),
    Map: () => import("@/components/blocks/Map.vue"),
  },
  computed: {
    getLines() {
      return [
        {
          name: "Маршрут 1",
          color: "#3EA2FF",
          coords: [
            [54.321359161031516, 48.35641169946904],
            [54.32767188858022, 48.35735604341745],
            [54.33136705345341, 48.36471907771376],
            [54.33543621661961, 48.37701556743433],
          ],
        },
      ];
    },

    getRegions() {
      return [
        {
          name: "Участок 1",
          temp: "-10",
          color: "#FF3D00",
          coords: [
            [54.34083658818023, 48.37933990021062],
            [54.32721226339364, 48.358049236646465],
            [54.321400516417576, 48.40217585387217],
          ],
        },
        {
          name: "Участок 2",
          temp: "-12",
          color: "#FFE600",
          coords: [
            [54.31542178141554, 48.35580825805665],
            [54.30781089651895, 48.33091735839844],
            [54.297193364198115, 48.338642120361335],
            [54.302702802966856, 48.35409164428712]
          ],
        },
      ];
    },
    getSnowplows() {
      return [
        {
          name: 'Бульдозер 1',
          status: 'Свободен',
          coords: [54.31782492633192, 48.39726448059083]
        },
        {
          name: 'Бульдозер 2',
          status: 'Свободен',
          coords: [54.30746036133708, 48.3889389038086]
        },
        {
          name: 'Бульдозер 3',
          status: 'Свободен',
          coords: [54.30330378805017, 48.330745697021484]
        }
      ]
    }
  },
  methods: {
    selectedRG(name) {
      if(this.selectRG === name) {
        this.selectRG = null
        return
      }
      this.selectRG = name
    },
    selectedSP(name) {
      if(this.selectSP === name) {
        this.selectSP = null
        return
      }
      this.selectSP = name
    }
  }
};
</script>

<style lang='scss'>
.dashboard {
  background: var(--bg_0);
}
</style>
