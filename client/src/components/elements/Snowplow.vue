<template lang='pug'>
  Element.snowplow(v-bind='$attrs' @click='onClick')
    Flex(col :gap='0' padding='0')
      h4 {{ snowplow.name }}
      span.snowplow_status {{ snowplow.status }}
</template>

<script>
export default {
  name: 'Snowplow',
  components: {
    Element: () => import('@/components/templates/Element.vue')
  },
  props: {
    snowplow: {
      type: Object,
      default: () => {
        return {
          name: 'Без названия'
        }
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
.snowplow {
  cursor: pointer;
  &_status {
    font-family: Ubuntu;
    font-style: normal;
    font-weight: 300;
    font-size: 12px;
    line-height: 19px;
    color: #BBBEC7;
  }
  &_icon {
    color: #BBBEC7;
    font-size: 20px;
  }
}
</style>