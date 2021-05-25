const onElementReady = $element => (
    new Promise((resolve) => {
      const waitForElement = () => {
        if ($element) {
          resolve($element);
        } else {
          window.requestAnimationFrame(waitForElement);
        }
      };
      waitForElement();
    })
);

export default onElementReady;
