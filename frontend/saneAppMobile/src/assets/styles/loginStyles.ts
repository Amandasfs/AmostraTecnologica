import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    padding: 24,
    justifyContent: 'center',
    alignItems: 'center',
  },
  logo: {
    width: 120,
    height: 120,
    marginBottom: 12,
    resizeMode: 'contain',
  },  
  title: {
    fontSize: 32,
    fontFamily: 'TitanOne_400Regular',
    marginBottom: 8,
    color: '#ff5900',
    textShadowColor: 'rgba(0, 0, 0, 0.1)',
    textShadowOffset: { width: 1, height: 1 },
    textShadowRadius: 2,
  },
  subtitle: {
    fontSize: 24,
    fontFamily: 'TitanOne_400Regular',
    marginBottom: 24,
    color: '#ff5900',
  },
  label: {
    alignSelf: 'flex-start',
    marginBottom: 4,
    fontFamily: 'Raleway',
    fontWeight: '300',
    color: '#ff5900',
  },
  input: {
    width: '100%',
    borderWidth: 1,
    borderColor: '#ff5900',
    borderRadius: 8,
    paddingHorizontal: 12,
    paddingVertical: 10,
    marginBottom: 16,
    backgroundColor: '#fff',
    shadowColor: '#000',
    shadowOffset: { width: 1, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  inputFocused: {
    borderColor: '#FF8C00',
    shadowOpacity: 0.3,
  },
  button: {
    marginTop: 12,
    backgroundColor: '#ff5900',
    paddingVertical: 12,
    paddingHorizontal: 32,
    borderRadius: 10,
    elevation: 2,
    shadowColor: '#FFA500',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
  },
  buttonText: {
    color: '#fff',
    fontFamily: 'TitanOne_400Regular',
    fontSize: 16,
    textAlign: 'center',
  },
  registerLink: {
    marginTop: 16,
    color: '#ff5900',
    fontFamily: 'Raleway',
    fontWeight: '300',
    textDecorationLine: 'underline',
  },
  registerBold: {
    fontWeight: 'bold',
  },
  forgotPasswordLink: {
    alignSelf: 'flex-end',
    color: '#ff5900',
    fontFamily: 'Raleway',
    fontWeight: '300',
    marginBottom: 12,
    textDecorationLine: 'underline',
  },

});

export default styles;
