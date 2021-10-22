<template lang='pug'>
Block(v-bind="$attrs", @mounted="init")
  #map(ref="map")
</template>

<script>
import "leaflet/dist/leaflet.css";
import L from "leaflet";

const snowIcon = require('@/assets/snow.png')
const bullIcon = require('@/assets/bull.png')

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
    lines: {
      type: Array,
      default: () => [],
    },
    snowplows: {
      type: Array,
      default: () => [],
    },
    selectRG: {
      type: String,
      default: null,
    },
    selectSP: {
      type: String,
      default: null,
    },
    selectLine: {
      type: String,
      default: null,
    },
  },
  data: () => {
    return {
      map: null,
      polygones: [],
      polylines: [],
      snowbulls: [],
    };
  },
  watch: {
    regions() {
      this.makeRegions();
    },
    lines() {
      this.makeLines();
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
      this.snowbulls.forEach((bull) => {
        if (bull.name === val) {
          this.map.setView(bull.coords, 18);
        }
      });
    },
    selectLine(val) {
      this.polylines.forEach((line) => {
        if (line.name === val) {
          line.obj.setStyle({ color: "#3EA2FF" });
          this.map.fitBounds(line.obj.getBounds());
        } else {
          line.obj.setStyle({ color: line.color });
        }
      });
    },
  },
  methods: {
    init() {
      this.map = L.map(this.$refs.map);

      L.tileLayer(
        "https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png",
        {
          subdomains: "abcd",
          minZoom: 0,
          maxZoom: 20,
        }
      ).addTo(this.map);
      L.tileLayer(
        "https://stamen-tiles-{s}.a.ssl.fastly.net/toner-hybrid/{z}/{x}/{y}{r}.{ext}",
        {
          subdomains: "abcd",
          minZoom: 10,
          maxZoom: 20,
          ext: "png",
          opacity: 0.5,
        }
      ).addTo(this.map);

      this.map.setView([54.3282, 48.3866], 13);
      this.makeRegions();
      this.makeLines();
      this.makeSnowplows()
    },
    makeRegions() {
      this.regions.forEach((region) => {
        const icon = L.icon({
          iconUrl: snowIcon,
          iconAnchor: [17, 55],
        })
        // eslint-disable-next-line new-cap
        const marker = new L.marker(region.coords[0], { icon })
        this.map.addLayer( marker );
        this.polygones.push({
          name: region.name,
          color: region.color,
          obj: L.polygon(region.coords, { color: region.color }).addTo(this.map).on('click', () => {
            this.$emit('selectedRG', region.name)
          }),
        });
      });
    },
    makeLines() {
      this.lines.forEach((line) => {
        this.polylines.push({
          name: line.name,
          color: line.coords,
          obj: L.polyline(line.coords, {
            color: line.color,
            weight: 6,
          }).addTo(this.map),
        });
      });
    },
    makeSnowplows() {
      const icon = L.icon({
        iconUrl: bullIcon,
        iconAnchor: [20, 55],
      })
      this.snowplows.forEach((bull) => {
        this.snowbulls.push({
          ...bull,
          // eslint-disable-next-line new-cap
          marker: new L.marker(bull.coords, { icon }).addTo(this.map).on('click', () => {
            this.$emit('selectedSP', bull.name)
          }),
        });
      });
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
</style>