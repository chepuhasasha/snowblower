<template lang='pug'>
  Flex.element(width='fill' :class='getClasses' justify-content='space-between' align-items='center' @click='onClick')
    slot
</template>

<script>
export default {
  name: 'Element',
  props: {
    active: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    getClasses() {
      return {
        [this.$style.active]: this.active
      }
    }
  },
  methods: {
    onClick() {
      this.$emit('click')
    }
  }
}
</script>

<style lang='scss'>
.element {
  background: var(--bg_100);
  border-color: var(--primary_100);
  border: 1px solid var(--bg_100);
  &:hover {
    border-color: var(--primary_100);
  }
}
</style>
<style lang="scss" module>
.active {
  background: var(--bg_0);
  border-color: var(--primary_100);
  &:hover {
    background: var(--bg_100);
  }
}
</style>