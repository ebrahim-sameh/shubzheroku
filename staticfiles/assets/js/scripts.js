let items = document.querySelectorAll('.carousel .carousel-item')
let items1 = document.querySelectorAll('.carousel2 .carousel-item2')

items.forEach((el) => {
    const minPerSlide = 4
    let next = el.nextElementSibling
    for (var i=1; i<minPerSlide; i++) {
        if (!next) {
            // wrap carousel by using first child
        	next = items[0]
      	}
        let cloneChild = next.cloneNode(true)
        el.appendChild(cloneChild.children[0])
        next = next.nextElementSibling
    }
})


items1.forEach((e2) => {
  const minPerSlide = 4
  let next2 = e2.nextElementSibling
  for (var i=1; i<minPerSlide; i++) {
      if (!next2) {
          // wrap carousel by using first child
        next2 = items1[0]
      }
      let cloneChild = next2.cloneNode(true)
      e2.appendChild(cloneChild.children[0])
      next2 = next2.nextElementSibling
  }
})
