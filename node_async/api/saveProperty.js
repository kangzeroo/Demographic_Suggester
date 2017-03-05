const Property = require('../models/property_model');

exports.savePropertyToDb = function(property){
  const p = new Promise((res, rej)=>{
    const prop = new Property(property);
    prop.save(function(err, savedProperty){
      if(err){
        console.log(err)
        rej(err)
      }
      console.log("=========== SAVING PROPERTY TO DB ===========")
      res(savedProperty)
    })
  })
  return p
}
