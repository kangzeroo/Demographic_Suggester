export function filterRegex(queryString){
  const p = new Promise((res, rej)=>{
    const tags = filterStuff(queryString)
    res(tags)
  })
  return p
}


function filterStuff(queryString){
	const matches = queryString.match(/(young)|(student)|(music)|(fit)|(hacking)|(vibrant)|(cultural)|(professional)|(nerd)|(outgoing)|(sports)|(school)|(ambitious)|(laid back)|(budget)/ig)
  if(matches){
    const tags = matches.map((m)=>{
      console.log(m)
      return {
        tag_word: m
      }
    })
    return tags
  }else{
    return []
  }
}
