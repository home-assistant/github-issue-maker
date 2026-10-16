Add [significant change](https://contributors.home-assistant.io/core/integrations/significant-change/) support to the {{ DOMAIN }} integration. All official properties need to be taken into consideration when deciding if a change is significant. If the integration has device classes, they should be taken into consideration and tested.

See the [contributor documentation](https://contributors.home-assistant.io/core/entities/{{ DOMAIN }}/) for more information about the entity properties and device classes.

For an example of a significant change platform, see [the light integration](https://github.com/home-assistant/core/blob/dev/homeassistant/components/light/significant_change.py) and it's [tests](https://github.com/home-assistant/core/blob/dev/tests/components/light/test_significant_change.py). For example on how to differentiate based on device classes, see [the sensor integration](https://github.com/home-assistant/core/blob/dev/homeassistant/components/sensor/significant_change.py).

To get started with this issue, you will need to set up a Home Assistant development environment. The easiest approach is to get started using [a dev container](https://contributors.home-assistant.io/core/development/environment/#development-container).

Once you have a development environment set up, run the following and follow the instructions:

```python
python3 -m script.scaffold significant_change
```
