<template lang='pug'>
  Flex(col width='fill').temp
    Flex(padding='0' align-items='center')
      icon.temp_icon(icon='map-marker-alt')
      h2 {{ city }}
    Flex(padding='0' align-items='center' :gap='10')
      h1 {{ temp }}°C
      icon.temp_icon__big(icon='snowflake')
</template>

<script>
export default {
  name: 'Temp',
  props: {
    temp: {
      type: String,
      default: '0'
    },
    city: {
      type: String,
      default: () => 0
    }
  }
}
</script>

<style lang='scss'>
.temp {
  &_icon {
    font-size: 16px;
    color: #FFFFFF;
    &__big {
      font-size: 36px;
      color: #FFFFFF;
    }
  }
}
</style>