<template lang='pug'>
Block(v-bind="$attrs", @mounted="init")
  #map(ref="map")
</template>

<script>
import "leaflet/dist/leaflet.css";
import L from "leaflet";
import 'leaflet-openweathermap'


const city = require('./city.json')
const points = require('./points.json')
const snowIcon = require("@/assets/snow.png");
const bullIcon = require("@/assets/bull.png");

export default {
  name: "Map",
  components: {
    Block: () => import("@/components/templates/Block.vue"),
  },
  props: {
    regions: {
      type: Array,
      default: () => [],
    },
    cars: {
      type: Array,
      default: () => [],
    },
    selectRG: {
      type: String,
      default: null,
    },
    selectSP: {
      type: Number,
      default: null,
    },
    polygone: {
      trpe: Object,
      default: null
    }
  },
  data: () => {
    return {
      map: null,
      region: null,
      polygones: [],
      polylines: [],
      carsData: [],
      garage: [
        [52.61907391770899, 39.522621567470935],
        [52.61915208081608, 39.53154983340855],
        [52.61568671567549, 39.53163568211949],
        [52.61563460282798, 39.52266449182641],
      ]
    };
  },
  watch: {
    regions() {
      this.makeRegions();
    },
    cars() {
      this.makeCars();
    },
    selectRG(val) {
      this.polygones.forEach((polygon) => {
        if (polygon.name === val) {
          polygon.obj.setStyle({ color: "#3EA2FF" });
          this.map.fitBounds(polygon.obj.getBounds());
        } else {
          polygon.obj.setStyle({ color: polygon.color });
        }
      });
    },
    selectSP(val) {
      this.cars.forEach((bull) => {
        if (bull.id === val) {
          this.map.setView(bull.coord, 18);
        }
      });
    },
    "polygone.a.lat": function(val){
      console.log(val)
      this.makePolygon()
    },
    "polygone.b.lat": function(val){
      console.log(val)
      this.makePolygon()
    },
    "polygone.c.lat": function(val){
      console.log(val)
      this.makePolygon()
    },
    "polygone.d.lat": function(val){
      console.log(val)
      this.makePolygon()
    }
  },
  methods: {
    init() {
      const CartoDB_DarkMatter = L.tileLayer(
        "https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png",
        {
          subdomains: "abcd",
          minZoom: 0,
          maxZoom: 20,
        }
      );
      const Stamen_TonerHybrid = L.tileLayer(
        "https://stamen-tiles-{s}.a.ssl.fastly.net/toner-hybrid/{z}/{x}/{y}{r}.{ext}",
        {
          subdomains: "abcd",
          minZoom: 13,
          maxZoom: 20,
          ext: "png",
          opacity: 0.5,
        }
      );

      const apiKey = "a42629671608e1ce16b722c374588553";
      const clouds = L.OWM.clouds({
        showLegend: false,
        opacity: 0.05,
        appId: apiKey,
      });
      const precipitationcls = L.OWM.precipitationClassic({
        showLegend: false,
        appId: apiKey,
        opacity: 0.8,
      });
      const snow = L.OWM.snow({
        showLegend: false,
        opacity: 0.8,
        appId: apiKey,
      });
      const temp = L.OWM.temperature({ showLegend: false, appId: apiKey });

      const overlayMaps = {
        Облока: clouds,
        Осадки: precipitationcls,
        Снег: snow,
        Температура: temp,
        Дороги: Stamen_TonerHybrid,
      };
      this.map = L.map(this.$refs.map, {
        layers: [
          CartoDB_DarkMatter,
          Stamen_TonerHybrid,
          precipitationcls,
          clouds,
        ],
      });
      this.region = L.polygon([], { color: 'red' }).addTo(this.map)
      // eslint-disable-next-line new-cap
      L.control.layers({}, overlayMaps).addTo(this.map);
      this.map.setView([52.60311, 39.57076], 13);
      L.polygon(city.coords, { 
        color: '#3EA2FF',
        fill: false
      }).addTo(this.map)
      this.makeGarage()
      this.makePoints()
      this.makeRegions();
      this.makeCars();
      this.map.on('click', (e) => {
         this.$emit('click', e)
      })
    },
    makeGarage() {
      L.polygon(this.garage, { color: 'red' }).addTo(this.map)
    },
    makeRegions() {
      this.regions.forEach((region) => {
        const icon = L.icon({
          iconUrl: snowIcon,
          iconAnchor: [17, 55],
        });
        // eslint-disable-next-line new-cap
        const marker = new L.marker(region.coords[0], { icon });
        this.map.addLayer(marker);
        this.polygones.push({
          name: region.name,
          color: region.color,
          obj: L.polygon(region.coords, { color: region.color })
            .addTo(this.map)
            .on("click", () => {
              this.$emit("selectedRG", region.name);
            }),
        });
      });
    },
    makeCars() {
      const icon = L.icon({
        iconUrl: bullIcon,
        iconAnchor: [20, 55],
      });
      if(!this.carsData[0]){
        this.cars.forEach((car) => {
          this.carsData.push({
            ...car,
            // eslint-disable-next-line new-cap
            marker: new L.marker(car.coord, { icon }).addTo(this.map).on("click", () => {
              this.$emit("selectedSP", car.id);
            }),
            line: car.way ? L.polyline(car.way, {
              color: '#3EA2FF',
              weight: 6,
            }).addTo(this.map) : null
          });
        });
      } else {
        this.cars.forEach(car => {
          this.carsData.forEach(lcar => {
            if(lcar.id == car.id) {
              lcar.marker.setLatLng(car.coord)
            }
          })
        })
      }
    },
    makePoints() {
      L.polyline(points, {
              color: '#3EA2FF',
              opacity: 0.5,
              weight: 6,
            }).addTo(this.map)
    },
    makePolygon() {
      const coords = []
      if(this.polygone) {
        if(this.polygone.a.lat) {
          coords.push([this.polygone.a.lat, this.polygone.a.lng])
        }
        if(this.polygone.b.lat) {
          coords.push([this.polygone.b.lat, this.polygone.b.lng])
        }
        if(this.polygone.c.lat) {
          coords.push([this.polygone.c.lat, this.polygone.c.lng])
        }
        if(this.polygone.d.lat) {
          coords.push([this.polygone.d.lat, this.polygone.d.lng])
        }
      }
      this.region.setLatLngs(coords)
      
    }
  },
};
</script>

<style lang='scss'>
#map {
  background: var(--bg_0);
  width: 100%;
  height: 100%;
}

.leaflet-control-zoom-in,
.leaflet-control-zoom-out {
  background: #1a1a1a !important;
  border-bottom: none !important;
  &:hover {
    background: #3ea2ff !important;
    color: white !important;
  }
}
.leaflet-control-layers-separator {
  border-top: none;
}

.leaflet-control {
  border: none !important;
  background: #1a1a1a;
  a,
  span {
    font-family: Ubuntu !important;
    color: #ababab;
    font-size: 12px !important;
  }
}
</style>