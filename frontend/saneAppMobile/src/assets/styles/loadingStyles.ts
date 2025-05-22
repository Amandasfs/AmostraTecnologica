import { StyleSheet } from 'react-native';

export default StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  logo: {
    width: 200,
    height: 200,
    resizeMode: 'contain',
  },
  loadingBar: {
    marginTop: 20,
  },
  loadingText: {
    marginTop: 12,
    fontSize: 16,
    color: '#ff5900',
    fontFamily: 'TitanOne_400Regular',
  },
  defaultText: {
    fontSize: 16,
    fontFamily: 'Raleway_200ExtraLight',
    color: '#000',
  },
});
