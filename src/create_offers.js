function generateOffer(storeItems, amt, offerTypes = null, multiple = false) {
  if (offerTypes === null) {
    return generateOfferWithAnyOfferType(storeItems, amt, multiple);
  } else {
    return generateOfferWithMultipleOfferTypes(storeItems, amt, offerTypes, multiple);
  }
}

function generateOfferWithAnyOfferType(storeItems, amt, multiple) {
  let cache = new Map();

  const setCache = (storeItems, amt, offer) => {
    storeItems = [...storeItems].sort();

    let hashItem = [amt, ...storeItems]; // Todo: Better way to hash
    if (cache.get(hashItem) !== undefined) {
      throw 'Cache Already Exists. Ideally, you shouldn\'t have reached here.';
    }
    cache.set(hashItem, offer);
  }

  const fetchCache = (storeItems, amt) => {
    storeItems = [...storeItems].sort();
    let hashItem = [amt, ...storeItems]; // Todo: Better way to hash

    return cache.get(hashItem);
  }

  const generateOfferWithMultipleItems = (storeItems, amt) => {
    if (amt < 0) {
      return false;
    } else if (amt === 0) {
      return [];
    }

    let cachedResult = fetchCache(storeItems, amt);
    if (cachedResult !== undefined) {
      return cachedResult;
    }

    for (let item of storeItems) {
      let remainingStoreItems = new Set(storeItems);
      remainingStoreItems.delete(item);

      let offer = generateOfferWithMultipleItems(remainingStoreItems, amt - item.price);
      if (offer !== false) {
        offer = [...offer, item];
        setCache(storeItems, amt, offer);
        return new Set(offer);
      }
    }

    setCache(storeItems, amt, false);
    return false;
  }

  const generateOfferWithSingleItem = (storeItems, amt) => {
    for (let item in storeItems) {
      if (item.price === amt) {
        return new Set([item]);
      }
    }
    return false; // Item Not Found
  }

  return (multiple)
    ? generateOfferWithMultipleItems(storeItems, amt)
    : generateOfferWithSingleItem(storeItems, amt);
}

function generateOfferWithMultipleOfferTypes(storeItems, amt, offerTypes, multiple) {
  // storeItems.offerTypes is an Array

  let cache = new Map();

  const setCache = (storeItems, amt, offerTypes, offer) => {
    storeItems = [...storeItems].sort();
    offerTypes = [...offerTypes].sort();

    let hashItem = [amt, ...storeItems, ...offerTypes]; // Todo: Better way to hash
    if (cache.get(hashItem) !== undefined) {
      throw 'Cache Already Exists. Ideally, you shouldn\'t have reached here.';
    }
    cache.set(hashItem, offer);
  }

  const fetchCache = (storeItems, amt, offerTypes) => {
    offerTypes = [...offerTypes].sort();
    storeItems = [...storeItems].sort();

    let hashItem = [amt, ...storeItems, ...offerTypes]; // Todo: Better way to hash

    return cache.get(hashItem);
  }

  const generateOfferWithMultipleItems = (storeItems, amt, offerTypes) => {
    if (amt < 0) {
      return false;
    } else if (amt === 0) {
      return (offerTypes.size === 0)
        ? []
        : false;
    }

    let cachedResult = fetchCache(storeItems, amt, offerTypes);
    if (cachedResult !== undefined) {
      return cachedResult;
    }

    for (let item of storeItems) {
      let remainingStoreItems = new Set(storeItems);
      remainingStoreItems.delete(item);

      let remainingOfferTypes = new Set(offerTypes);
      item.offerTypes.forEach((offerType) => {
        remainingOfferTypes.delete(offerType);
      });

      let offer = generateOfferWithMultipleItems(remainingStoreItems, amt - item.price, remainingOfferTypes);
      if (offer !== false) {
        offer = [...offer, item];
        setCache(storeItems, amt, offerTypes, offer);
        return new Set(offer);
      }
    }

    setCache(storeItems, amt, offerTypes, false);
    return false;
  }

  const isSet1SubsetOfSet2 = (set1, set2) => {
    for (let item of set1) {
      if (!set2.has(item)) {
        return false;
      }
    }
    return true;
  }

  const generateOfferWithSingleItem = (storeItems, amt, offerTypes) => {
    // storeItems.offerTypes is an Array

    for (let item of storeItems) {
      if (item.price === amt && isSet1SubsetOfSet2(offerTypes, new Set(item.offerTypes))) {
        return new Set([item]);
      }
    }
  }

  return (multiple)
    ? generateOfferWithMultipleItems(storeItems, amt, offerTypes)
    : generateOfferWithSingleItem(storeItems, amt, offerTypes);
}

module.exports.generateOffer = generateOffer;
module.exports.generateOfferWithAnyOfferType = generateOfferWithAnyOfferType;
module.exports.generateOfferWithMultipleOfferTypes = generateOfferWithMultipleOfferTypes;

//export { generateOffer, generateOfferWithAnyOfferType, generateOfferWithMultipleOfferTypes };
