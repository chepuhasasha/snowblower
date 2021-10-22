<template lang='pug'>
  Flex.dashboard(padding="20px", width="fill", height="fill")
    Block(title="Участки", width="fill", height="fill")
</template>

<script>
export default {
  name: 'Home',
  components: {
    Block: () => import("@/components/templates/Block.vue"),
  },
}
</script>
<style lang='scss'>
.dashboard {
  background: var(--bg_0);
}
</style>