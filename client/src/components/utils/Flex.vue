<template lang='pug'>
component(:is="tag", :style="getStyle", @click="onClick")
  slot
</template>

<script>
export default {
  name: "Flex",
  props: {
    tag: {
      type: String,
      default: "div",
    },
    col: {
      type: Boolean,
      default: false,
    },
    gap: {
      type: Number,
      default: 10,
    },
    padding: {
      type: String,
      default: "10px",
    },
    width: {
      type: String,
      default: "hug",
      validator: (value) => {
        return ["hug", "fill"].includes(value);
      },
    },
    fixWidth: {
      type: Number,
      default: null,
    },
    height: {
      type: String,
      default: "hug",
      validator: (value) => {
        return ["hug", "fill"].includes(value);
      },
    },
    fixheight: {
      type: Number,
      default: null,
    },
    justifyContent: {
      type: String,
      default: "start",
      validator: (value) => {
        return [
          "start",
          "center",
          "space-around",
          "space-between",
          "end",
        ].includes(value);
      },
    },
    justifySelf: {
      type: String,
      default: "start",
      validator: (value) => {
        return ["start", "center", "end"].includes(value);
      },
    },
    alignItems: {
      type: String,
      default: "start",
      validator: (value) => {
        return ["start", "center", "end"].includes(value);
      },
    },
    alignSelf: {
      type: String,
      default: "start",
      validator: (value) => {
        return ["start", "center", "end"].includes(value);
      },
    },
    overflow: {
      type: String,
      default: null
    }
  },
  computed: {
    getStyle() {
      const map = {
        hug: "max-content",
        fill: "100%",
      };
      return {
        display: "flex",
        flexDirection: this.col ? "column" : "row",
        gap: `${this.gap}px`,
        padding: this.padding,
        width: this.fixWidth ? `${this.fixWidth}px` : map[this.width],
        height: this.fixHeight ? `${this.fixHeight}px` : map[this.height],
        justifyContent: this.justifyContent,
        justifySelf: this.justifySelf,
        alignItems: this.alignItems,
        alignSelf: this.alignSelf,
        overflow: this.overflow ? this.overflow : 'none'
      };
    },
  },
  methods: {
    onClick() {
      this.$emit("click");
    },
  },
  mounted() {
    this.$emit("mounted");
  },
};
</script>

<style lang='scss' scoped>
</style>