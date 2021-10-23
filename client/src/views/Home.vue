<template lang='pug'>
Flex.dashboard(padding="20px", width="fill", height="fill")
  Flex(col, padding="0", :fixWidth="300", height="fill")
    Temp(:temp="wather", city="Липицк")
    Block(title="Участок", width="fill", height="fill")
      Region(
        v-for="(region, i) in getRegions",
        :region="region",
        :key="i",
        :active="selectRG === region.name",
        @click="selectedRG(region.name)"
      )
      Flex(
        col,
        padding="0",
        width="fill",
        align-items="center",
        justify-content="center",
        @click="addPoly = !addPoly"
      ) 
        Flex(
          padding="0",
          width="fill",
          align-items="center",
          justify-content="center",
          @click="addPoly = !addPoly"
        ) 
          input(placeholder="lat", type="number", v-model="polygone.a.lat")
          input(placeholder="lng", type="number", v-model="polygone.a.lng")
          button(
            @click="setPoint('a')",
            :class="{ active: activePoint === 'a' }"
          )
            icon(icon="crosshairs")
        Flex(
          padding="0",
          width="fill",
          align-items="center",
          justify-content="center",
          @click="addPoly = !addPoly"
        ) 
          input(placeholder="lat", type="number", v-model="polygone.b.lat")
          input(placeholder="lng", type="number", v-model="polygone.b.lng")
          button(
            @click="setPoint('b')",
            :class="{ active: activePoint === 'b' }"
          )
            icon(icon="crosshairs")
        Flex(
          padding="0",
          width="fill",
          align-items="center",
          justify-content="center",
          @click="addPoly = !addPoly"
        ) 
          input(placeholder="lat", type="number", v-model="polygone.c.lat")
          input(placeholder="lng", type="number", v-model="polygone.c.lng")
          button(
            @click="setPoint('c')",
            :class="{ active: activePoint === 'c' }"
          )
            icon(icon="crosshairs")
        Flex(
          padding="0",
          width="fill",
          align-items="center",
          justify-content="center",
          @click="addPoly = !addPoly"
        ) 
          input(placeholder="lng", type="number", v-model="polygone.d.lng")
          input(placeholder="lat", type="number", v-model="polygone.d.lat")
          button(
            @click="setPoint('d')",
            :class="{ active: activePoint === 'd' }"
          )
            icon(icon="crosshairs")
        Flex(
          tag="button",
          padding="10px 13px",
          width="fill",
          align-items="center",
          justify-content="center",
          @click="setPolygone"
        ) Рассчитать маршруты
  Map(
    title="Карта",
    width="fill",
    height="fill",
    @click="mapClick",
    :regions="getRegions",
    :cars="getCars",
    :selectRG="selectRG",
    :selectSP="selectSP",
    :polygone="this.polygone",
    @selectedRG="selectedRG($event)",
    @selectedSP="selectedSP($event)"
  )
  Block(title="Техника", :fixWidth="300", height="fill")
    Snowplow(
      v-for="(car, i) in getCars",
      :snowplow="car",
      :key="i",
      :active="selectSP === car.id",
      @click="selectedSP(car.id)"
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
      addPoly: false,
      activePoint: null,
      wather: 0,
      polygone: {
        a: { lat: null, lng: null },
        b: { lat: null, lng: null },
        c: { lat: null, lng: null },
        d: { lat: null, lng: null },
      },
      cars: [],
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
    mapClick(e) {
      if (this.activePoint) {
        this.polygone[this.activePoint].lat = e.latlng.lat;
        this.polygone[this.activePoint].lng = e.latlng.lng;
      }
    },
    setPolygone() {
      console.log('расчитать запрос');
    },
    setPoint(name) {
      this.activePoint = name;

      console.log(name);
    },
    getData() {
      axios.get("http://178.154.229.18:8000/api/venicle").then((res) => {
        this.cars = res.data;
      });
      axios.get("https://api.openweathermap.org/data/2.5/weather?q=London&appid=e08f8129f4a0dc9d6ff18b259c5ff81c").then((res) => {
        this.wather = Math.round(res.data.main.temp -273)
        console.log(this.wather)
      });

    },
  },
  mounted() {
    this.getData();
    setInterval(() => {
      this.getData();
    }, 10000);
  },
};
</script>

<style lang='scss'>
.dashboard {
  background: var(--bg_0);
}
.active {
  background: var(--primary_0);
}
</style>
