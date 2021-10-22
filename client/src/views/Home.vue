<template lang='pug'>
Flex.dashboard(padding="20px", width="fill", height="fill")
  Flex(col, padding="0", :fixWidth="300", height="fill")
    Temp(temp="-16", city="Липитск")
    Block(title="Участки", width="fill", height="fill")
      Region(
        v-for="(region, i) in getRegions",
        :region="region",
        :key="i",
        :active="selectRG === region.name",
        @click="selectedRG(region.name)"
      )
    Block(title="Техника", width="fill", height="fill")
      Snowplow(
        v-for="(car, i) in getCars",
        :snowplow="car",
        :key="i",
        :active="selectSP === car.id",
        @click="selectedSP(car.id)"
      )
    Block(title="Настройки", width="fill")
  Map(
    title="Карта",
    width="fill",
    height="fill",
    :regions="getRegions",
    :cars="getCars",
    :selectRG="selectRG",
    :selectSP="selectSP",
    @selectedRG="selectedRG($event)",
    @selectedSP="selectedSP($event)"
  )
</template>

<script>
import axios from "axios";

export default {
  name: "Home",
  data: () => {
    return {
      selectRG: null,
      selectSP: null,
      cars: []
    };
  },
  components: {
    Block: () => import("@/components/templates/Block.vue"),
    Region: () => import("@/components/elements/Region.vue"),
    Snowplow: () => import("@/components/elements/Snowplow.vue"),
    Temp: () => import("@/components/blocks/Temp.vue"),
    Map: () => import("@/components/blocks/Map.vue"),
  },
  computed: {
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
    getCars() {
      return this.cars;
    },
  },
  methods: {
    selectedRG(id) {
      if (this.selectRG === id) {
        this.selectRG = null;
        return;
      }
      this.selectRG = id;
    },
    selectedSP(id) {
      if (this.selectSP === id) {
        this.selectSP = null;
        return;
      }
      this.selectSP = id;
    },
    getData() {
      axios
        .get("https://api.coindesk.com/v1/bpi/currentprice.json")
        .then(() => {
          this.cars = [
            {
              id: 1,
              name: "Бульдозер максим",
              number: "АУ777Е",
              status: "В работе",
              coords: [52.60283902179348, 39.5168277094808],
              way: [
                [52.594706282077965, 39.50395579982881],
                [52.609198189273584, 39.5296996191328],
                [52.605758098557764, 39.53278887744928],
                [52.60409007851464, 39.53793764131006],
              ],
            },
          ];
        });
    },
  },
  mounted() {
    setInterval(()=> {
      this.getData();
    },1000)
  },
};
</script>

<style lang='scss'>
.dashboard {
  background: var(--bg_0);
}
</style>
