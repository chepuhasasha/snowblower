<template lang='pug'>
  Flex.block(col padding='0' :gap='0' v-bind='$attrs')
    Flex.block_header(align-items='center' width='fill' )
      h3.block_title {{ title }}
      Flex(padding='0')
        slot(name='tools')
    Flex.block_body(col :gap='5' width='fill' height='fill' @mounted='$emit("mounted")')
      slot
</template>

<script>
export default {
  name: 'Block',
  props: {
    title: {
      type: String,
      default: 'Название'
    }
  }
}
</script>

<style lang='scss'>
.block {
  background: var(--bg_0);
  border: 1px solid var(--bg_200);
  &_header {
    background: var(--bg_100);
  }
  &_body {
    height: 100%;
    overflow: auto;
  }
}
</style>

<style lang='scss' module='mode'>
</style>