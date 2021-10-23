<template lang='pug'>
  Element.region(v-bind='$attrs' @click='onClick' :style='getStyle')
    h4 {{ region.name }}
    Flex(align-items='center' :gap='5' padding='0')
      icon.region_icon(icon='snowflake')
      span.region_temp {{ region.temp }}°C
</template>

<script>
export default {
  name: 'Region',
  components: {
    Element: () => import('@/components/templates/Element.vue')
  },
  props: {
    region: {
      type: Object,
      default: () => {
        return {
          name: 'Без названия'
        }
      }
    }
  },
  computed: {
    getStyle(){
      return {
        borderLeft: `2px solid ${this.region.color}`
      }
    }
  },
  methods: {
    onClick() {
      this.$emit('click')
    },
  }
}
</script>

<style lang='scss'>
.region {
  cursor: pointer;
  &_temp {
    font-family: Ubuntu;
    font-style: normal;
    font-weight: 300;
    font-size: 16px;
    line-height: 19px;
    color: #BBBEC7;
  }
  &_icon {
    color: #BBBEC7;
    font-size: 20px;
  }
}
</style>