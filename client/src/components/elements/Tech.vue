<template lang='pug'>
  Element.region(v-bind='$attrs' @click='test')
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
  methods: {
    test() {
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
    font-size: 26px;
  }
}
</style>