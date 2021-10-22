<template lang='pug'>
Flex.dashboard(padding="20px", width="fill", height="fill")
  Flex(col, padding="0", :fixWidth="300", height="fill")
    Temp(temp='-16' city='Липитск')
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
        // {
        //   name: "Маршрут 1",
        //   color: "#3EA2FF",
        //   coords: [],
        // },
      ];
    },

    getRegions() {
      return [
        // {
        //   name: "Участок 1",
        //   temp: "-10",
        //   color: "#FF3D00",
        //   coords: [],
        // },
        // {
        //   name: "Участок 2",
        //   temp: "-12",
        //   color: "#FFE600",
        //   coords: [],
        // },
      ];
    },
    getSnowplows() {
      return [
        // {
        //   name: 'Бульдозер 1',
        //   status: 'Свободен',
        //   coords: [54.31782492633192, 48.39726448059083]
        // },
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
