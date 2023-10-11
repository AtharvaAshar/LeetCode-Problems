/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    const throwError = (errorStr)=> {throw new Error(errorStr)}

    return {
        toBe: (v) => v===val || throwError("Not Equal"),
        notToBe: (v) => v!==val || throwError("Equal")
    }
    
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */