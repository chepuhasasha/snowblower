const lipick = {
  left: 52.66389056542804,
  right: 52.66305767075937,
  bottom: 52.52624809700062,
  top:  39.439770774506606
}

const result = []
let w = (lipick.right - lipick.left) / 10
let h = (lipick.bottom - lipick.top) / 10

for(let i = 0; i < 10; i++) {
  for(let j = 0; j < 10; j++) {
    let zone = {
      left: lipick.left + (j * w),
      right: lipick.left + (j * w) + w,
      bottom: lipick.top + (i * h),
      top: lipick.top + (i * h) + h
    }
    result.push(zone)
  }
}

console.log(result)